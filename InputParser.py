

class InputParser:

    def __init__(self):
        pass

    def parse_ids_from_file(self, file_path):
        """
        parse ids from files
        :param file_path: file path
        :return: ids to requests
        """
        ids = []
        with open(file_path, 'r') as f:
            for id in f.readlines():
                ids.append(id.strip())
        return ids