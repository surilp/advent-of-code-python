from utils.utils import file_to_collection


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))


class Fold:
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value


class TransparentOrigami:

    def __init__(self, input_file):
        self.folds = []
        self.dots = set()
        self.max_x = -float('inf')
        self.max_y = -float('inf')
        self._process_raw_data(input_file)

    def _process_raw_data(self, input_file):
        raw_data = file_to_collection(input_file)
        for item in raw_data:
            if item:
                if 'fold' in item:
                    axis, value = item.replace('fold along ', '').split('=')
                    self.folds.append(Fold(axis, int(value)))
                else:
                    x, y = item.split(',')
                    self.max_x = max(self.max_x, int(x))
                    self.max_y = max(self.max_y, int(y))
                    self.dots.add(Point(int(x), int(y)))

    def go_through_folds(self, num_of_folds):
        for num, fold in enumerate(self.folds):
            if num_of_folds and num >= num_of_folds:
                break
            self.max_x = -float('inf')
            self.max_y = -float('inf')
            temp_set = set()
            while self.dots:
                cur_dot = self.dots.pop()
                self._add_new_location(cur_dot, fold, temp_set)
            self.dots = temp_set

    def _add_new_location(self, dot, fold, temp_set):
        if fold.axis == 'y' and dot.y > fold.value:
            new_y = self._new_loc_helper(dot.y, fold.value)
            dot.y = new_y
        elif fold.axis == 'x' and dot.x > fold.value:
            new_x = self._new_loc_helper(dot.x, fold.value)
            dot.x = new_x
        self.max_x = max(self.max_x, dot.x)
        self.max_y = max(self.max_y, dot.y)
        temp_set.add(dot)

    def _new_loc_helper(self, axis_value, fold_value):
        diff = axis_value - fold_value
        new_val = fold_value - diff
        return new_val

    def part1(self, num_of_folds=1):
        self.go_through_folds(num_of_folds)
        return len(self.dots)

    def part2(self, num_of_folds=0):
        self.go_through_folds(num_of_folds)
        self.print_dots()
        return len(self.dots)

    def print_dots(self):
        temp_dots = self.dots.copy()
        matrix = [['.'] * (self.max_x + 1) for _ in range(self.max_y + 1)]
        while temp_dots:
            cur_dot = temp_dots.pop()
            matrix[cur_dot.y][cur_dot.x] = '#'
        for item in matrix:
            print(item)
