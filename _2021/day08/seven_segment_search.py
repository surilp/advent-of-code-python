from utils.utils import file_to_collection
from collections import defaultdict


class Entry:

    def __init__(self, signal_patterns, four_digit_output):
        self.final_map = self. _process_data(signal_patterns)
        self.four_digit_output = [''.join(sorted(item)) for item in four_digit_output]


    def get_output(self):
        result = 0
        for digit in self.four_digit_output:
            temp = self.final_map[digit]
            result = result * 10 + temp
        return result

    def _process_data(self, signal_patterns):
        num_to_signal_map = {}
        to_be_process_signals_by_len = defaultdict(list)
        segment_value_map = defaultdict(set)
        for signal in signal_patterns:
            signal = set(signal)
            if len(signal) == 2:
                num_to_signal_map[1] = signal
            elif len(signal) == 3:
                num_to_signal_map[7] = signal
            elif len(signal) == 4:
                num_to_signal_map[4] = signal
            elif len(signal) == 7:
                num_to_signal_map[8] = signal
            else:
                length = len(signal)
                to_be_process_signals_by_len[length].append(signal)

        self._get_top(segment_value_map, num_to_signal_map)
        self._get_bottom_and_bottom_left(segment_value_map, num_to_signal_map, to_be_process_signals_by_len)
        self._get_top_right(segment_value_map, num_to_signal_map, to_be_process_signals_by_len)
        self._get_bottom_right(segment_value_map, num_to_signal_map)
        num_to_signal_map[9] = num_to_signal_map[4].union(segment_value_map['bottom'],
                                                                    segment_value_map['top'])
        num_to_signal_map[0] = [item for item in to_be_process_signals_by_len[6] if
                                     item not in [num_to_signal_map[6], num_to_signal_map[9]]][0]
        self._get_middle(segment_value_map, num_to_signal_map)
        self._get_top_left(segment_value_map, num_to_signal_map)
        num_to_signal_map[2] = num_to_signal_map[8].difference(segment_value_map['top_left'],
                                                                         segment_value_map['bottom_right'])
        num_to_signal_map[3] = num_to_signal_map[8].difference(segment_value_map['top_left'],
                                                                         segment_value_map['bottom_left'])
        num_to_signal_map[5] = num_to_signal_map[8].difference(segment_value_map['top_right'],
                                                                         segment_value_map['bottom_left'])
        return {''.join(sorted(list(v))): k for k,v in num_to_signal_map.items()}


    def _get_bottom_and_bottom_left(self, segment_value_map, num_to_signal_map, to_be_process_signals_by_len):
        for segment in num_to_signal_map[8].difference(num_to_signal_map[7].union(num_to_signal_map[4])):
            is_bottom = all([segment in item for item in to_be_process_signals_by_len[5]])
            if is_bottom:
                segment_value_map['bottom'] = {segment}
            else:
                segment_value_map['bottom_left'] = {segment}

    def _get_top(self, segment_value_map, num_to_signal_map):
        segment_value_map['top'] = num_to_signal_map[7].difference(num_to_signal_map[1])

    def _get_top_right(self, segment_value_map, num_to_signal_map, to_be_process_signals_by_len):
        for item in to_be_process_signals_by_len[6]:
            result = num_to_signal_map[7].difference(item)
            if result:
                segment_value_map['top_right'] = result
                num_to_signal_map[6] = item.copy()
                break

    def _get_bottom_right(self, segment_value_map, num_to_signal_map):
        segment_value_map['bottom_right'] = num_to_signal_map[1].difference(
            segment_value_map['top_right'])

    def _get_middle(self, segment_value_map, num_to_signal_map):
        segment_value_map['middle'] = num_to_signal_map[8].difference(num_to_signal_map[0])

    def _get_top_left(self, segment_value_map, num_to_signal_map):
        segment_value_map['top_left'] = num_to_signal_map[4].difference(
            num_to_signal_map[7].union(segment_value_map['middle']))


class SevenSegmentSearch:
    seg_to_num_map = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9
    }

    def __init__(self, input_file):
        self.raw_data = list(map(self._process_item, file_to_collection(input_file)))
        self.len_of_segment_map = self._segment_len()
        pass

    def _process_item(self, item):
        item = item.split('|')
        entry = Entry(item[0].split(), item[1].split())
        return entry

    def _segment_len(self):
        result = defaultdict(list)
        for segment, _ in SevenSegmentSearch.seg_to_num_map.items():
            result[len(segment)].append(SevenSegmentSearch.seg_to_num_map[segment])
        return result

    def part1(self):
        result = 0
        len_to_be_searched = [k for k, v in self.len_of_segment_map.items() if len(v) == 1]
        for entry in self.raw_data:
            for digit in entry.four_digit_output:
                if len(digit) in len_to_be_searched:
                    result += 1
        return result

    def part2(self):
        result = 0
        for entry in self.raw_data:
            result += entry.get_output()
        return result
