from utils.utils import file_to_collection
from collections import defaultdict

class Lanternfish:

    def __init__(self, input_file):
        self.input_file = input_file
        self.main_dict = defaultdict(int)
        self.process_data()
        self.days_processed = 0

    def process_data(self):
        for fish_age in map(int, file_to_collection(self.input_file)[0].split(',')):
            self.main_dict[fish_age] += 1

    def reproduce(self, num_of_days):
        days = num_of_days
        while days != self.days_processed:
            temp_dict = defaultdict(int)
            for key,val in self.main_dict.items():
                if key == 0:
                    temp_dict[8] += val
                    temp_dict[6] += val
                else:
                    temp_dict[key-1] += val
            self.main_dict = temp_dict
            days -= 1
        self.days_processed = num_of_days

    def get_result(self, num_of_days):
        result = 0
        self.reproduce(num_of_days)
        for key,val in self.main_dict.items():
            result += val
        return result



