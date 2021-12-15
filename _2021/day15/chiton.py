from utils.utils import file_to_collection
from utils.heap import Heap


class Chiton:

    def __init__(self, input_file, factor):
        self.grid = Grid(self._process_data(input_file), factor)
        self.distance = [[float('inf')] * (self.grid.col_size) for _ in range(self.grid.row_size)]
        self.distance[0][0] = 0
        self.heap = Heap(lambda x, y: self.distance[x[0]][x[1]] < self.distance[y[0]][y[1]])
        self.heap.push((0, 0))
        self.visited = set()

    def _process_data(self, input_file):
        return [list(map(int, list(row))) for row in file_to_collection(input_file)]

    def _find_distance(self):
        while not self.heap.is_empty():
            cur_row, cur_col = self.heap.pop()
            if (cur_row, cur_col) in self.visited:
                continue
            self.visited.add((cur_row, cur_col))
            for inc_row, inc_col in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                new_row, new_col = cur_row + inc_row, cur_col + inc_col
                if 0 <= new_row < len(self.distance) and 0 <= new_col < len(self.distance[0]):
                    if self.distance[cur_row][cur_col] + self.grid[(new_row, new_col)] < self.distance[new_row][
                        new_col]:
                        self.distance[new_row][new_col] = self.distance[cur_row][cur_col] + self.grid[
                            (new_row, new_col)]
                        self.heap.push((new_row, new_col))

    def result(self):
        self._find_distance()
        return self.distance[-1][-1]


class Grid:

    def __init__(self, data, factor):
        self.grid = data
        self.grid_row_size = len(self.grid)
        self.grid_col_size = len(self.grid[0])
        self.row_size = self.grid_row_size * factor
        self.col_size = self.grid_col_size * factor

    def __getitem__(self, location):
        loc_row, loc_col = location
        if 0 <= loc_row < self.row_size and 0 <= loc_col < self.col_size:
            loc_row, row_val_to_be_added = self._loc_helper(loc_row, 'row')
            loc_col, col_val_to_be_added = self._loc_helper(loc_col, 'col')
            result = (self.grid[loc_row][loc_col] + row_val_to_be_added + col_val_to_be_added)
            if result > 9:
                result = (result + 1) % 10
            return result
        else:
            raise Exception('index out of bound')

    def _loc_helper(self, loc, axis):
        new_loc = loc % self.grid_row_size if axis in ['row'] else loc % self.grid_col_size
        new_add = loc // self.grid_row_size if axis in ['row'] else loc // self.grid_col_size
        return new_loc, new_add
