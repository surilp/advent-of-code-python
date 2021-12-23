from collections import deque, defaultdict

DOT = '0'
HASH = '1'


def get_data_from_file(input_file):
    data = open(input_file).read().split('\n\n')
    image_enhancement_algo = data[0].replace('#', HASH).replace('.', DOT)
    input_image = list(map(list, data[1].replace('#', HASH).replace('.', DOT).split('\n')))
    return image_enhancement_algo, input_image


def part1(input_file, enhance_num):
    algo, pixels = get_data_from_file(input_file)
    background_bit = DOT
    for _ in range(enhance_num):
        pixels = _bfs(algo, pixels, background_bit)
        background_bit = DOT if algo[0] == DOT or background_bit == HASH else HASH
    return len([1 for row in pixels for col in row if col == HASH])


def _bfs(algorithm, pixels, background_bit):
    queue = deque()
    queue.append((0, 0))
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    result_dict = {}
    min_row, min_col = float('inf'), float('inf')
    max_row, max_col = -float('inf'), -float('inf')
    while queue:
        current = queue.popleft()
        if current in result_dict:
            continue
        row_idx, col_idx = current
        current_pixel_neighbors = [(row_idx + neighbor[0], col_idx + neighbor[1]) for neighbor in neighbors]
        binary = get_binary_for_pixel(current_pixel_neighbors, pixels, background_bit)
        min_row = min(min_row, row_idx)
        min_col = min(min_col, col_idx)
        max_row = max(max_row, row_idx)
        max_col = max(max_col, col_idx)
        result_dict[(row_idx, col_idx)] = algorithm[int(binary, 2)]
        queue.extend(filter_pixels(current_pixel_neighbors, 0, len(pixels), 0, len(pixels[0])))
    return dict_to_pixels(result_dict, min_row, max_row, min_col, max_col)


def dict_to_pixels(dict, min_row, max_row, min_col, max_col):
    row_booster = 0 - min_row
    col_booster = 0 - min_col

    row_size = max_row + row_booster + 1
    col_size = max_col + col_booster + 1

    result = [[DOT] * col_size for _ in range(row_size)]

    for pixel, value in dict.items():
        pixel_row, pixel_col = pixel
        pixel_row += row_booster
        pixel_col += col_booster

        result[pixel_row][pixel_col] = value
    # print_pixels(result)
    return result


def filter_pixels(pixels, min_row, max_row, min_col, max_col):
    result = list(
        filter(lambda pix: min_row - 3 <= pix[0] < max_row + 3 and min_col - 3 <= pix[1] < max_col + 3, pixels))
    return result


def get_binary_for_pixel(current_pixel_neighbors, pixels, background_bit):
    binary = [get_binary_digit(current, pixels, background_bit) for current in current_pixel_neighbors]
    return ''.join(binary)


def get_binary_digit(pixel, pixels, background_bit):
    pixel_row, pixel_col = pixel
    if 0 <= pixel_row < len(pixels) and 0 <= pixel_col < len(pixels[0]):
        return pixels[pixel_row][pixel_col]
    else:
        return background_bit


def print_pixels(pixels):
    for p in pixels:
        print(p)
