from utils.utils import file_to_collection
from math import sqrt
from collections import defaultdict


def get_beacons_for_each_scanner(input_file):
    raw_data = file_to_collection(input_file)
    beacons = set()
    scanners = []
    for line in raw_data:
        if line:
            if '---' not in line:
                x, y, z = list(map(int, line.split(',')))
                beacons.add((x, y, z))
            else:
                if beacons:
                    scanners.append(beacons)
                    beacons = set()
    if beacons:
        scanners.append(beacons)
    return scanners


def calculate_distance(beacon1, beacon2):
    b2_x, b2_y, b2_z = beacon2
    b1_x, b1_y, b1_z = beacon1
    return int(sqrt((b2_x - b1_x) ** 2 + (b2_y - b1_y) ** 2 + (b2_z - b1_z) ** 2))


def subtract_beacon_from_centroid(centroid, beacon):
    c_x, c_y, c_z = centroid
    b1_x, b1_y, b1_z = beacon
    return (round(b1_x - c_x, 4), round(b1_y - c_y, 4), round(b1_z - c_z, 4))


def subtract_beacon_from_centroid2(centroid, beacon):
    c_x, c_y, c_z = centroid
    b1_x, b1_y, b1_z = beacon
    return (b1_x - c_x, b1_y - c_y, b1_z - c_z)


def add_beacon_to_centroid(beacon, centroid):
    c_x, c_y, c_z = centroid
    b1_x, b1_y, b1_z = beacon
    return (round(b1_x + c_x), round(b1_y + c_y), round(b1_z + c_z))


def calculate_centroid(beacons):
    x_centroid = sum([b_x for b_x, _, _ in beacons]) / len(beacons)
    y_centroid = sum([b_y for _, b_y, _ in beacons]) / len(beacons)
    z_centroid = sum([b_z for _, _, b_z in beacons]) / len(beacons)
    return (x_centroid, y_centroid, z_centroid)


def scanners_beacon_to_beacon_distance(beacons):
    result = defaultdict(set)
    for b1 in beacons:
        for b2 in beacons:
            if b1 != b2:
                result[b1].add(calculate_distance(b1, b2))
    return result


def compare_scanner_beacons_with_base_scanner_beacons(base_scanner_beacons, target_scanner_beacons):
    match = []
    for b1, b1_distances in base_scanner_beacons.items():
        for b2, b2_distances in target_scanner_beacons.items():
            intersection = set(b1_distances).intersection(b2_distances)
            match.append(len(intersection))
    return max(match)


def get_common_beacons(base_scanner_beacons, target_scanner_beacons):
    base_beacon_to_target_beacon_common = defaultdict(tuple)
    for b1, b1_distances in base_scanner_beacons.items():
        for b2, b2_distances in target_scanner_beacons.items():
            intersection = set(b1_distances).intersection(b2_distances)
            if len(intersection) >= 11:
                base_beacon_to_target_beacon_common[b1] = b2
    return base_beacon_to_target_beacon_common


def find_rotation_and_translation(common_beacons):
    base_beacon_centroid = calculate_centroid(common_beacons.keys())
    target_beacon_centroid = calculate_centroid(common_beacons.values())
    first_base_beacon = list(common_beacons.keys())[0]
    first_target_beacon = common_beacons[first_base_beacon]
    from_centroid_base_beacon = subtract_beacon_from_centroid(base_beacon_centroid, first_base_beacon)
    from_centroid_target_beacon = subtract_beacon_from_centroid(target_beacon_centroid, first_target_beacon)
    cord_location = [None, None, None]
    sign = [None, None, None]
    abs_from_centroid_base_beacon = list(map(abs, from_centroid_target_beacon))
    for t_idx, point in enumerate(from_centroid_base_beacon):
        idx = abs_from_centroid_base_beacon.index(abs(point))
        cord_location[t_idx] = idx
        if point == from_centroid_target_beacon[cord_location[t_idx]]:
            sign[t_idx] = 1
        else:
            sign[t_idx] = -1
    transformed_target_beacon_centroid = [None, None, None]
    for idx in range(len(transformed_target_beacon_centroid)):
        transformed_target_beacon_centroid[idx] = target_beacon_centroid[cord_location[idx]] * sign[idx]
    return cord_location, sign, base_beacon_centroid, tuple(transformed_target_beacon_centroid)


def transform_target_beacon(target_beacon, cord_location, sign, base_beacon_centroid, target_beacon_centroid):
    transformed_beacon = [None, None, None]
    for idx in range(len(transformed_beacon)):
        transformed_beacon[idx] = target_beacon[cord_location[idx]] * sign[idx]
        transformed_beacon[idx] = transformed_beacon[idx] - target_beacon_centroid[idx]
        transformed_beacon[idx] = round(transformed_beacon[idx] + base_beacon_centroid[idx])
    return tuple(list(map(int, transformed_beacon)))


def transform_scanner_beacons(base_scanner, target_scanner, cord_location, sign, base_beacon_centroid,
                              target_beacon_centroid):
    temp = []
    for beacon in target_scanner:
        transformed_beacon = transform_target_beacon(beacon, cord_location, sign, base_beacon_centroid,
                                                     target_beacon_centroid)
        temp.append(transformed_beacon)
        base_scanner.add(transformed_beacon)
    pass


def part1(input_file):
    scanners_with_beacons = get_beacons_for_each_scanner(input_file)
    scanner_location = [(0, 0, 0)]
    base_scanner = scanners_with_beacons.pop(0)
    while scanners_with_beacons:
        base_scanners_with_beacons_distances = scanners_beacon_to_beacon_distance(base_scanner)
        scanners_with_beacons_distances = []
        for _, beacons in enumerate(scanners_with_beacons):
            scanners_with_beacons_distances.append(scanners_beacon_to_beacon_distance(beacons))
        scanner_matches = []
        for idx in range(len(scanners_with_beacons_distances)):
            scanner_matches.append(
                compare_scanner_beacons_with_base_scanner_beacons(base_scanners_with_beacons_distances,
                                                                  scanners_with_beacons_distances[idx]))
        scanner_to_evaluate = scanner_matches.index(max(scanner_matches))
        common_beacons = get_common_beacons(base_scanners_with_beacons_distances,
                                            scanners_with_beacons_distances[scanner_to_evaluate])
        cord_location, sign, base_beacon_centroid, target_beacon_centroid = find_rotation_and_translation(
            common_beacons)
        scanner_location.append(
            transform_target_beacon((0, 0, 0), cord_location, sign, base_beacon_centroid, target_beacon_centroid))
        transform_scanner_beacons(base_scanner, scanners_with_beacons.pop(scanner_to_evaluate), cord_location, sign,
                                  base_beacon_centroid, target_beacon_centroid)
    return len(base_scanner), scanner_location


def taxicab_distance(scanner1, scanner2):
    s1_x, s1_y, s1_z = scanner1
    s2_x, s2_y, s2_z = scanner2
    return abs(s2_x - s1_x) + abs(s2_y - s1_y) + abs(s2_z - s1_z)

def largest_taxicab_distance(scanners):
    result = -float('inf')
    for s1 in scanners:
        for s2 in scanners:
            result = max(result, taxicab_distance(s1, s2))
    return result
