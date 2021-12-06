def sonar_sweep(input_file):
    result = 0
    with open(input_file, 'r') as file:
        prev_depth = None
        depth = int(file.readline().strip())
        while depth:
            if prev_depth and depth > prev_depth:
                result += 1
            prev_depth = depth
            depth = file.readline().strip()
            depth = int(depth) if depth else None
    return result


def window_sonar_sweep(input_file):
    result = 0

    window = [None, None, None]
    current_sum = 0
    prev_sum = None
    counter = 0
    with open(input_file, 'r') as file:
        depth = int(file.readline().strip())
        while depth:
            if counter < 3:
                window[counter] = depth
                current_sum += depth
                counter += 1
            else:
                prev_sum = current_sum
                current_sum -= window[0]
                window[0] = window[1]
                window[1] = window[2]
                window[2] = depth
                current_sum += window[2]
                if prev_sum and current_sum > prev_sum:
                    result += 1

            depth = file.readline().strip()
            depth = int(depth) if depth else None
    return result
