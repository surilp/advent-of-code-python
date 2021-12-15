from utils.utils import file_to_collection
from collections import defaultdict, Counter
from math import ceil


class Polymerization:

    def __init__(self, input_file):
        self.template = None
        self.pairs = defaultdict(str)
        self._process_file_data(input_file)
        self.cache = defaultdict(str)
        pass

    def _process_file_data(self, input_file):
        raw_data = file_to_collection(input_file)
        for item in raw_data:
            if item:
                if '->' in item:
                    pair, insertion = item.split('->')
                    pair = pair.strip()
                    insertion = insertion.strip()
                    self.pairs[pair] = insertion
                else:
                    self.template = item

    def _grow_polymer(self, steps):
        cur_step = 1
        while cur_step <= steps:
            self.template = self._grow_polymer_helper(self.template)
            cur_step += 1

    def _grow_polymer_helper(self, template):
        if template in self.cache:
            return self.cache[template]
        template_len = len(template)
        if template_len >= 2:
            if template_len == 2:
                return f'{template[0]}{self.pairs[template]}{template[-1]}'
            elif template_len == 3:
                self.cache[template] = template[0] + self.get_pair_result(template[:2]) + self.get_pair_result(
                    template[1:])
                return self.cache[template]
            mid = template_len // 2
            self.cache[template] = self._grow_polymer_helper(template[:mid]) + self.get_pair_result(
                template[mid - 1:mid + 1]) + self._grow_polymer_helper(template[mid:])[1:]
            return self.cache[template]

    def get_pair_result(self, pair):
        if pair in self.pairs:
            return self.pairs[pair] + pair[-1]

    def final_result(self, steps=10):
        self._grow_polymer(steps)
        counter = Counter(self.template)
        max_c = -float('inf')
        min_c = float('inf')
        for _, count in counter.items():
            max_c = max(count, max_c)
            min_c = min(count, min_c)
        return max_c - min_c


def final_result(input_file, steps):
    raw_data = file_to_collection(input_file)
    lookup = {}
    for item in raw_data:
        if item:
            if '->' in item:
                pair, insertion = item.split('->')
                pair = pair.strip()
                insertion = insertion.strip()
                lookup[pair] = insertion
            else:
                template = item
    left = 0
    right = 1
    template_len = len(template)
    result_dict = defaultdict(int)
    while right < template_len:
        cur_pair = template[left:right + 1]
        if cur_pair in lookup:
            result_dict[cur_pair[0] + lookup[cur_pair]] += 1
            result_dict[lookup[cur_pair] + cur_pair[1]] += 1
        else:
            result_dict[cur_pair] += 1
        left += 1
        right += 1
    cur_step = 2
    while cur_step <= steps:
        temp_dict = defaultdict(int)
        for pair, count in result_dict.items():
            if pair in lookup:
                temp_dict[pair[0] + lookup[pair]] += 1 * count
                temp_dict[lookup[pair] + pair[1]] += 1 * count
            else:
                temp_dict[pair] += 1 * count
        result_dict = temp_dict
        cur_step += 1
    letter_dict = defaultdict(int)
    for pair, count in result_dict.items():
        letter_dict[pair[0]] += count
        letter_dict[pair[1]] += count
    max_num = -float('inf')
    min_num = float('inf')
    for let, count in letter_dict.items():
        max_num = max(max_num, ceil(count / 2))
        min_num = min(min_num, ceil(count / 2))
    return max_num - min_num
