from utils.utils import file_to_collection
from math import ceil, floor
import ast
from copy import deepcopy


class SnailFish:

    def __init__(self, input_file):
        self.snail_fish_numbers = list(map(ast.literal_eval, file_to_collection(input_file)))

    def process(self):
        return SnailFish.sum_snail_fish_numbers(self.snail_fish_numbers)

    def part1_magnitude(self):
        return SnailFish.calculate_magnitude(SnailFish.sum_snail_fish_numbers(self.snail_fish_numbers))

    @staticmethod
    def sum_snail_fish_numbers(numbers):
        if len(numbers) in [0, 1]:
            return numbers
        cur = 1
        result = numbers[0]
        while cur < len(numbers):
            result = SnailFish.add_snail_Fish_numbers(result, numbers[cur])
            cur += 1
        return result

    @staticmethod
    def add_snail_Fish_numbers(num1, num2):
        result = [num1, num2]
        SnailFish.explode_split_snail_fish_number(result)
        return result

    @staticmethod
    def explode_split_snail_fish_number(snail_fish_number):
        while True:
            updated = [False]
            SnailFish.explode_helper(snail_fish_number, 1, updated)
            if not updated[0] and not SnailFish.split_num(snail_fish_number):
                break

    @staticmethod
    def explode_helper(number, depth, updated):
        if depth == 4:
            for idx in range(len(number)):
                item = number[idx]
                if isinstance(item, list):
                    left, right = None, None
                    number[idx] = 0
                    if idx > 0:
                        SnailFish.add_number(number, idx - 1, item[0], 'left')
                    else:
                        left = item[0]
                    if idx < len(number) - 1:
                        SnailFish.add_number(number, idx + 1, item[1], 'right')
                    else:
                        right = item[1]
                    return item, left, right
            return (None, None, None)

        for idx in range(len(number)):
            if isinstance(number[idx], list):
                updated_num, left, right = SnailFish.explode_helper(number[idx], depth + 1, updated)
                if left:
                    if idx != 0:
                        SnailFish.add_number(number, idx - 1, left, 'left')
                        left = None
                if right:
                    if idx != len(number) - 1:
                        SnailFish.add_number(number, idx + 1, right, 'right')
                        right = None
                if updated_num:
                    updated[0] = True
                    return (None, left, right)
                elif updated[0]:
                    return (None, left, right)
        return (None, None, None)

    @staticmethod
    def add_number(number, idx, value, dir):
        if isinstance(number[idx], int):
            number[idx] += value
        elif isinstance(number[idx], list):
            number = number[idx]
            if dir == "left":
                while isinstance(number[-1], list):
                    number = number[-1]
                number[-1] += value
            elif dir == "right":
                while isinstance(number[0], list):
                    number = number[0]
                number[0] += value

    @staticmethod
    def split_num(number):
        for idx in range(len(number)):
            if isinstance(number[idx], int) and number[idx] >= 10:
                to_be_split = number[idx] / 2
                number[idx] = [floor(to_be_split), ceil(to_be_split)]
                return True
            elif isinstance(number[idx], list):
                if SnailFish.split_num(number[idx]):
                    return True

    @staticmethod
    def calculate_magnitude(number):
        if isinstance(number, list):
            if isinstance(number[0], int) and isinstance(number[1], int):
                return (3 * number[0]) + (2 * number[1])
            elif isinstance(number[0], int) and isinstance(number[1], list):
                return (3 * number[0]) + (2 * SnailFish.calculate_magnitude(number[1]))
            elif isinstance(number[0], list) and isinstance(number[1], int):
                return (3 * SnailFish.calculate_magnitude(number[0])) + (2 * number[1])
            else:
                return (3 * SnailFish.calculate_magnitude(number[0])) + (2 * SnailFish.calculate_magnitude(number[1]))

    @staticmethod
    def largest_magnitude(numbers):
        max_magnitude = -float('inf')
        for outer_idx in range(len(numbers)):
            for inner_idx in range(len(numbers)):
                if outer_idx == inner_idx:
                    continue
                x = numbers[outer_idx]
                y = numbers[inner_idx]
                max_magnitude = max(
                    SnailFish.calculate_magnitude(SnailFish.add_snail_Fish_numbers(deepcopy(x), deepcopy(y))),
                    max_magnitude)
        return max_magnitude

    def max_magnitude_part2(self):
        return SnailFish.largest_magnitude(self.snail_fish_numbers)
