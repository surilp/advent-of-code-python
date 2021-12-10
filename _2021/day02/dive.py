from utils.utils import file_to_collection


def dive(input_file):
    input = file_to_collection(input_file)
    horizontal_position = 0
    vertical_position = 0

    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

    for item in input:
        direction, value = item.split()
        value = int(value)
        if direction == FORWARD:
            horizontal_position += value
        elif direction == DOWN:
            vertical_position += value
        elif direction == UP:
            vertical_position -= value
        else:
            raise Exception(f'{direction} direction is not supported')

    return horizontal_position * vertical_position

def dive2(input_file):
    input = file_to_collection(input_file)
    horizontal_position = 0
    vertical_position = 0
    aim = 0

    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

    for item in input:
        direction, value = item.split()
        value = int(value)
        if direction == FORWARD:
            horizontal_position += value
            vertical_position += aim * value
        elif direction == DOWN:
            aim += value
        elif direction == UP:
            aim -= value
        else:
            raise Exception(f'{direction} direction is not supported')

    return horizontal_position * vertical_position
