from utils.utils import file_to_collection
from collections import defaultdict,Counter

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
            elif template_len ==3:
                self.cache[template] = template[0] + self.get_pair_result(template[:2]) + self.get_pair_result(template[1:])
                return self.cache[template]
            mid = template_len//2
            self.cache[template] = self._grow_polymer_helper(template[:mid]) + self.get_pair_result(template[mid-1:mid+1]) + self._grow_polymer_helper(template[mid:])[1:]

            return self.cache[template]

    def get_pair_result(self, pair):
        if pair in self.pairs:
            return self.pairs[pair] + pair[-1]


    def final_result(self, steps = 10):
        self._grow_polymer(steps)
        counter = Counter(self.template)
        max_c = -float('inf')
        min_c = float('inf')
        for _, count in counter.items():
            max_c = max(count, max_c)
            min_c = min(count, min_c)
        return max_c - min_c


