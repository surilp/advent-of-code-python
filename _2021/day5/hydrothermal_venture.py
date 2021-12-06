from utils.utils import file_to_collection


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_line(self, matrix, p2: 'point'):
        inc = self._get_incrementor(p2)
        cur_x, cur_y = self.x, self.y
        while cur_x != p2.x or cur_y != p2.y:
            matrix[cur_y][cur_x] += 1
            cur_x += inc.x
            cur_y += inc.y
        matrix[cur_y][cur_x] += 1

    def _get_incrementor(self, p2: 'Point'):
        result = [0, 0]
        if p2.x > self.x:
            result[0] = 1
        elif p2.x < self.x:
            result[0] = -1
        if p2.y > self.y:
            result[1] = 1
        elif p2.y < self.y:
            result[1] = -1
        return Point(result[0], result[1])


class HydrothermalVenture():

    def __init__(self, input_file):
        self.data = None
        self.input_file = input_file
        self.part1_points = []
        self.part2_points = []
        self._process_data()
        self.par1_result = 0
        self.par2_result = 0

    def _process_data(self):
        raw_data = file_to_collection(self.input_file)
        row_len = 0
        col_len = 0
        for item in raw_data:
            item = item.split('->')
            p1 = list(map(int, item[0].strip().split(',')))
            p2 = list(map(int, item[1].strip().split(',')))
            p1 = Point(p1[0], p1[1])
            p2 = Point(p2[0], p2[1])
            row_len = max(row_len, p1.y, p2.y)
            col_len = max(col_len, p1.x, p2.x)
            if p1.x == p2.x or p1.y == p2.y:
                self.part1_points.append([p1, p2])
            else:
                self.part2_points.append([p1, p2])
        row_len += 1
        col_len += 1
        self.data = [[0] * col_len for _ in range(row_len)]

    def get_part1_result(self):
        for p1, p2 in self.part1_points:
            p1.draw_line(self.data, p2)
        self.par1_result = self._get_result()
        return self.par1_result

    def get_part2_result(self):
        if not self.par1_result:
            self.get_part1_result()
        for p1, p2 in self.part2_points:
            p1.draw_line(self.data, p2)
        return self._get_result()

    def _get_result(self):
        result = 0
        for row_idx in range(len(self.data)):
            for col_idx in range(len(self.data[row_idx])):
                if self.data[row_idx][col_idx] > 1:
                    result += 1
        return result
