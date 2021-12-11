from utils.utils import file_to_collection


class DumboOctopus:
    NEIGHBORS = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]

    def __init__(self, input_file):
        self.grid = [list(map(int, list(row))) for row in file_to_collection(input_file)]
        self.grid_size = len(self.grid) * len(self.grid[0])
        self.set1 = set()
        self.set2 = set()
        self.flashed = set()
        self.flashes = 0
        self.all_flashed_at = None

    def _increase_energy_level(self, num_of_step):
        current_step = 1
        while current_step <= num_of_step:
            for row_idx in range(len(self.grid)):
                for col_idx in range(len(self.grid[0])):
                    self.grid[row_idx][col_idx] += 1
                    if self.grid[row_idx][col_idx] > 9:
                        self.set1.add((row_idx, col_idx))

            while self.set1 or self.set2:
                if self.set1:
                    current_octo = self.set1.pop()
                    self.flashed.add(current_octo)
                    self.flashes += 1

                    self._process_adjacent_octo(current_octo)
                else:
                    self.set1 = self.set2
                    self.set2 = set()

            if not self.all_flashed_at and len(self.flashed) == self.grid_size:
                self.all_flashed_at = current_step
                return

            while self.flashed:
                current_row, current_col = self.flashed.pop()
                self.grid[current_row][current_col] = 0

            current_step += 1

    def part1(self, num_of_steps=100):
        self._increase_energy_level(num_of_steps)
        return self.flashes

    def part2(self):
        self._increase_energy_level(float('inf'))
        return self.all_flashed_at

    def _process_adjacent_octo(self, octo):

        oct_row, oct_col = octo
        for neighbor_row, neighbor_col in DumboOctopus.NEIGHBORS:
            new_oct_row, new_oct_col = oct_row + neighbor_row, oct_col + neighbor_col
            new_oct = (new_oct_row, new_oct_col)
            if 0 <= new_oct_row < len(self.grid) and 0 <= new_oct_col < len(
                    self.grid[0]) and new_oct not in self.set1 and new_oct not in self.flashed:
                self.grid[new_oct_row][new_oct_col] += 1
                if self.grid[new_oct_row][new_oct_col] > 9:
                    self.set2.add((new_oct_row, new_oct_col))
