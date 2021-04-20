
import asyncio
import logging
import sys
import argparse
import configparser
from Client import Client
from SampleGenerator import SampleGenerator
from InputParser import InputParser

if __name__ == '__main__':
    # logger
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=logging.DEBUG,
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger("areq")
    logging.getLogger("chardet.charsetprober").disabled = True

    # read information from config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    requested_url = config['DEFAULT']['RequestedUrl']
    max_requests = int(config['DEFAULT']['Limit_requests'])
    test_file_dir = config['DEFAULT']['TestFileDir']
    result_file_dir = config['DEFAULT']['ResultFileDir']

    # argument parse and input
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--test_file', dest='path of test file')
    args = parser.parse_args()

    InputParser = InputParser()

    if not args.test_file:
        # generate samples
        sampleGenerator = SampleGenerator()
        test_file_path = sampleGenerator.generate_sample_files(test_file_dir, dup = False)

        # read ids
        ids = InputParser.parse_ids_from_file(test_file_path)
    else:
        try:
            ids = InputParser.parse_ids_from_file(args.test_file)
        except:
            logger.info("Error happen, --test_file not valid! Program terminated.")
            quit()

    # initialize client
    client = Client(requested_url, ids, max_requests, result_file_dir, logger)
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(client.run_requests())
    loop.run_until_complete(future)

    logger.info("Finished requesting!")
