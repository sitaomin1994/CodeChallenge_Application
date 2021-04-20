import random
import string


class SampleGenerator:

    def __init__(self, id_len=20, num_ids=50, seed=21):
        self.id_len = id_len
        self.num_ids = num_ids
        self.seed = seed
        random.seed(self.seed)

    def generate_random_id(self):
        """
        Generat one random id
        :return: base64 encoded id
        """
        id = ''.join([str(random.choice(string.ascii_letters)) for _ in range(self.id_len)])
        return id

    def generate_samples(self):
        """
        Generate test samples - ids
        :return: a list of random samples
        """
        random_ids = []
        random_ids.append("cRF2dvDZQsmu37WGgK6MTcL7XjH")
        for i in range(self.num_ids-1):
            random_ids.append(self.generate_random_id())
        return random_ids

    def generate_samples_dup(self, ratio=0.2):
        """
        Generate test samples with duplication ids
        :return: a list of random samples
        """
        random_ids = []
        for i in range(self.num_ids - int(self.num_ids * ratio)):
            random_ids.append(self.generate_random_id())

        dup_ids = []
        for i in range(int(self.num_ids * ratio)):
            dup_ids.append(random.choice(random_ids))

        return random_ids + dup_ids

    def generate_sample_files(self, test_file_dir, dup=True):
        """
        Generate test files with/o duplicated ids
        :param test_file_dir: file directory
        :param dup: whether to include duplicates
        :return: file name => string
        """
        if not dup:
            with open(test_file_dir + "sample.txt", "w") as f:
                f.write('\n'.join(self.generate_samples()))
            return test_file_dir + "sample.txt"
        else:
            with open(test_file_dir + "sample_dup.txt", "w") as f:
                f.write('\n'.join(self.generate_samples_dup()))
            return test_file_dir + "sample_dup.txt"