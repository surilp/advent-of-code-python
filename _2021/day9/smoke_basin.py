from utils.utils import file_to_collection
from functools import reduce

DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def smoke_basin(input_file):
    matrix = [[int(ele) for ele in row] for row in file_to_collection(input_file)]
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    result = [[], []]
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            if not visited[row_idx][col_idx]:
                _part1_dfs(matrix, visited, row_idx, col_idx, result)
    return result, matrix

def _part1_dfs(matrix, visited, row_idx, col_idx, result):
    if not visited[row_idx][col_idx]:
        visited[row_idx][col_idx] = True
        cur_row, cur_col = None, None
        smallest = True
        for inc_row, inc_col in DIRECTIONS:
            cur_row = row_idx + inc_row
            cur_col = col_idx + inc_col
            if 0 <= cur_row < len(matrix) and 0 <= cur_col < len(matrix[0]):
                if matrix[cur_row][cur_col] < matrix[row_idx][col_idx]:
                    _part1_dfs(matrix, visited, cur_row, cur_col, result)
                    smallest = False
                elif matrix[cur_row][cur_col] == matrix[row_idx][col_idx]:
                    smallest = False
                else:
                    visited[cur_row][cur_col] = True
        if smallest:
            result[1].append(matrix[row_idx][col_idx])
            result[0].append([row_idx, col_idx])


def part1_result(input_file):
    result, _ = smoke_basin(input_file)
    return sum(map(lambda num: num + 1, result[1]))

def part2_result(input_file):
    interim_result, matrix = smoke_basin(input_file)
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    result = []
    for cur_row, cur_col in interim_result[0]:
        current_result = [0]
        _part2_dfs(matrix, visited, cur_row, cur_col, current_result)
        result.append(current_result[0])
    result.sort(reverse=True)
    return reduce(lambda a, b: a*b, result[:3], 1)

def _part2_dfs(matrix, visited, row_idx, col_idx, result):
    if not visited[row_idx][col_idx] and matrix[row_idx][col_idx] != 9:
        visited[row_idx][col_idx] = True
        result[0] += 1
        for inc_row, inc_col in DIRECTIONS:
            cur_row = inc_row + row_idx
            cur_col = inc_col + col_idx
            if 0<= cur_row < len(matrix) and 0<=cur_col<len(matrix[0]):
                _part2_dfs(matrix, visited, cur_row, cur_col, result)


