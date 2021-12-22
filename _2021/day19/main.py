from beacon_scanner import part1, largest_taxicab_distance

part1_result, scanner_locations = part1('input.txt')

part2_result = largest_taxicab_distance(scanner_locations)

print(f'part 1 result - {part1_result}')
print(f'part 2 result - {part2_result}')