from utils.utils import file_to_collection

class Num():

    def __init__(self, num, board, row, col):
        self.key = num
        self.visited = False
        self.board_and_position = [[board, row, col]]

    def add_board_position(self, board, row, col):
        self.board_and_position.append([board, row, col])


class Board():

    def __init__(self, board_id, board_data, map):
        self.board_row_size = len(board_data)
        self.board_col_size = len(board_data[0])
        self.board_id = board_id
        self.board_data = board_data
        self.map = map
        self.process_data()
        self.result = None


    def process_data(self):
        for row_idx in range(len(self.board_data)):
            for col_idx in range(len(self.board_data[row_idx])):
                num = int(self.board_data[row_idx][col_idx])
                if num in self.map:
                    self.map[num].add_board_position(self.board_id, row_idx, col_idx)
                else:
                    self.map[num] = Num(num, self.board_id, row_idx, col_idx)
                self.board_data[row_idx][col_idx] = self.map[num]


class GiantSquid():
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = None
        self.boards = []
        self.map = {}
        self.process_data()


    def process_data(self):
        boards = []
        data = file_to_collection(self.input_file)
        temp = None
        for idx, item in enumerate(data):
            if idx == 0:
                self.numbers = [int(num) for num in item.split(',')]
            elif item == '':
                if temp:
                    boards.append(temp)
                temp = []
            else:
                item = item.split()
                temp.append(item)
        if temp:
            boards.append(temp)

        for idx,board_data in enumerate(boards):
            self.boards.append(Board(idx, board_data, self.map))

    def play_game(self, is_part1):
        part2_result = None
        for num in self.numbers:
            num_data = self.map[num]
            if not num_data.visited:
                num_data.visited = True
                for board, row, col in num_data.board_and_position:
                    if not self.boards[board].result and self._check_game_over(board, row, col):
                        if is_part1:
                            return self._final_result(num, board)
                        else:
                            part2_result = self._final_result(num, board)
        return part2_result

    def _check_game_over(self, board_idx, row_idx, col_idx):
        board = self.boards[board_idx].board_data
        row_visited = all([board[row_idx][col].visited for col in range(len(board[0]))])
        col_visited = all([board[row][col_idx].visited for row in range(len(board))])
        return row_visited or col_visited

    def _final_result(self, num, board_idx):
        board = self.boards[board_idx].board_data
        result = 0

        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                if not board[row_idx][col_idx].visited:
                    result += board[row_idx][col_idx].key
        self.boards[board_idx].result = result * num
        return self.boards[board_idx].result
