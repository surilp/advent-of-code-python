from utils.utils import file_to_collection
from collections import defaultdict
from statistics import median, mean

def treachery_of_whales(input_file, is_part2=False):
    crab_locations = list(map(int, file_to_collection(input_file)[0].split(',')))
    loc = mean(crab_locations) if is_part2 else median(crab_locations)
    loc = int(loc)
    loc_dict = defaultdict(int)
    for crab_loc in crab_locations:
        loc_dict[crab_loc] += 1
    result = 0
    for crab_loc, count in loc_dict.items():
        distance = get_part2_distance(crab_loc, loc) if is_part2 else get_part1_distance(crab_loc, loc)
        result += distance * count
    return result

def get_part1_distance(crab_loc, trial_location):
    return abs(crab_loc - trial_location)


def get_part2_distance(crab_loc, trial_location):
    distance = abs(crab_loc - trial_location)
    return (distance * (1 + distance)) // 2
