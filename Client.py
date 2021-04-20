import base64
import aiohttp
import asyncio
import aiofiles
import time


class Client:

    def __init__(self, base_url, ids, request_limits, result_file_dir, logger):

        self.base_url = base_url
        self.ids = ids
        self.max_request = request_limits
        self.connector = aiohttp.TCPConnector(limit=self.max_request)
        self.logger = logger
        self.processed_ids = set()
        self.result_file_dir = result_file_dir

    async def _request_one(self, url, header, id, index, session):
        """
        Request for one id
        :param url: str
        :param header: dict
        :param session: ClientSession
        :param id: str - requested id
        :return: None
        """
        async with session.get(url=url, headers=header) as resp:
            status = resp.status
            if status == '200':
                self.logger.info("[%s] Request for url %s, header: %s", index, url, header)
                result = await resp.text()

                # successful
                self.logger.info("[%s] [Successful] Request Success for url %s", index, url)
                if id not in self.processed_ids:
                    self.processed_ids.add(id)

                    async with aiofiles.open(self.result_file_dir + id + ".txt", "w") as f:
                        await f.write(result)
                        self.logger.info("[%s] Wrote results for source URL: %s",index, url)
            else:
                self.logger.info("[%s] [ERROR] Request error for url %s, status %s", index, url, resp.status)
                if resp == '429':
                    time.sleep(1000)

    async def run_requests(self):
        """
        Requests for all ids usnig async http request
        :return: None
        """
        loop = asyncio.get_event_loop()
        tasks = []
        async with aiohttp.ClientSession(connector=self.connector) as session:

            for index, id in enumerate(self.ids):
                if id not in self.processed_ids:
                    url = self.base_url + id
                    auth_token = base64.b64encode(id.encode('ascii'))
                    header = {"Authorization": auth_token.decode('UTF-8')}
                    tasks.append(asyncio.ensure_future(self._request_one(url=url, header=header, id=id, index = index, session = session)))

            _ = await asyncio.gather(*tasks)