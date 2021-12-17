from utils.utils import file_to_collection
from utils.math import Quadratic
from math import ceil, floor


class TrickShot:

    def __init__(self, input_file):
        self.x_range, self.y_range = self._get_range(input_file)
        pass

    def _get_range(self, input_file):
        data = file_to_collection(input_file)[0]
        x, y = data.replace('target area: ', '').split(', ')
        x = list(map(int, x.replace('x=', '').split('..')))
        y = list(map(int, y.replace('y=', '').split('..')))
        return x, y

    def part1(self):
        max_y = abs(self.y_range[0])
        return (max_y * (max_y - 1)) // 2

    def part2(self):
        result = []
        x_range = range(self.x_range[0], self.x_range[1] + 1)
        y_range = range(self.y_range[0], self.y_range[1] + 1)
        for x in range(self.x_range[1] + 1):
            for y in range(self.y_range[0], abs(self.y_range[0]) + 1):
                cur_x = 0
                del_x = x
                cur_y = 0
                del_y = y
                while cur_x not in x_range or cur_y not in y_range:
                    if del_x == 0 and cur_x not in x_range:
                        break
                    elif cur_y < self.y_range[0]:
                        break
                    if del_x > 0:
                        cur_x += del_x
                        del_x -= 1
                    elif del_x < 0:
                        cur_x += del_x
                        del_x += 1
                    cur_y += del_y
                    del_y -= 1
                else:
                    result.append((x,y))
        return len(result)