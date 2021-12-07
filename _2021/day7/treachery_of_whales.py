from utils.utils import file_to_collection
from collections import defaultdict


def treachery_of_whales(input_file, is_part2=False):
    crab_locations = map(int, file_to_collection(input_file)[0].split(','))
    loc_dict = defaultdict(int)
    min_loc, max_loc = float('inf'), -float('inf')
    for crab_loc in crab_locations:
        max_loc = max(max_loc, crab_loc)
        min_loc = min(min_loc, crab_loc)
        loc_dict[crab_loc] += 1
    result = float('inf')
    for trial_location in range(min_loc, max_loc + 1):
        current_result = 0
        for crab_loc, count in loc_dict.items():
            distance = get_part2_distance(crab_loc, trial_location) if is_part2 else get_part1_distance(crab_loc,
                                                                                                        trial_location)
            current_result += distance * count
        result = min(result, current_result)
    return result


def get_part1_distance(crab_loc, trial_location):
    return abs(crab_loc - trial_location)


def get_part2_distance(crab_loc, trial_location):
    distance = abs(crab_loc - trial_location)
    return (distance * (1 + distance)) // 2
