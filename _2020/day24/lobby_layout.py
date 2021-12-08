from utils.utils import file_to_collection
from functools import reduce

class LobbyLayout:
    DIRECTIONS = {'ne': [0.5, 1],
                  'e': [1, 0],
                  'se': [0.5, -1],
                  'sw': [-0.5, -1],
                  'w': [-1, 0],
                  'nw': [-0.5, 1]
                  }

    def __init__(self, input_file):
        self.input_data = map(self.parse_direction, file_to_collection(input_file))
        self.result_dict = {}

    def parse_direction(self, string):
        result = []
        temp = ''
        for char in string:
            temp += char
            if temp in LobbyLayout.DIRECTIONS:
                result.append(temp)
                temp = ''
        return result

    def run_part1(self):
        for directions in self.input_data:
            destination_tile = self.traverse_directions(directions)
            if destination_tile in self.result_dict:
                del self.result_dict[destination_tile]
            else:
                self.result_dict[destination_tile] = True
        return self.total_black_tiles()

    def run_part2(self, times):
        if not self.result_dict:
            self.run_part1()
        while times != 0:
            current_dict = {}
            for tile in self.result_dict.keys():
                self.traverse_adjacent_tiles(tile, current_dict)

            for tile, count in current_dict.items():
                if tile in self.result_dict and count not in [1,2]:
                    del self.result_dict[tile]
                elif tile not in self.result_dict and count == 2:
                    self.result_dict[tile] = True
            times -= 1

        return self.total_black_tiles()



    def total_black_tiles(self):
        return len(self.result_dict)

    def traverse_directions(self, directions):
        cur_x, cur_y = 0, 0
        for direction in directions:
            inc_x, inc_y = LobbyLayout.DIRECTIONS[direction]
            cur_x, cur_y = cur_x + inc_x, cur_y + inc_y
        return (float(cur_x), float(cur_y))

    def traverse_adjacent_tiles(self, tile, result):
        if tile not in result:
            result[tile] = 0
        tile_x, tile_y = tile
        for inc_x, inc_y in LobbyLayout.DIRECTIONS.values():
            cur_x, cur_y = tile_x + inc_x, tile_y + inc_y
            coordinate = (cur_x, cur_y)
            if coordinate in result:
                result[coordinate] += 1
            else:
                result[coordinate] = 1
