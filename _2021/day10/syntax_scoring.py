from utils.utils import file_to_collection
from statistics import median

POINT_MAP_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

POINT_MAP_2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

CLOSE_OPEN_MAP = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def syntax_scoring(input_file):
    data = file_to_collection(input_file)
    part1_result = 0
    part2_result = []
    for line in data:
        result = _find_first_incorrect_char_point(line)
        part1_result += result[0]
        if result[1]:
            part2_result.append(result[1])
    return part1_result, median(part2_result)


def _find_first_incorrect_char_point(line):
    stack = []
    for char in line:
        if char in '({[<':
            stack.append(char)
        else:
            if stack and stack[-1] == CLOSE_OPEN_MAP[char]:
                stack.pop()
            else:
                return POINT_MAP_1[char], 0
    part2_result = 0
    while stack:
        item = stack.pop()
        part2_result = (part2_result * 5) + POINT_MAP_2[item]
    return 0, part2_result
