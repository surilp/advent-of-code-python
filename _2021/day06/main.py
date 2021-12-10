from lanternfish import Lanternfish

l = Lanternfish('input.txt')

part1 = l.get_result(80)
part2 = l.get_result(256)

print(f'part 1 - {part1}')
print(f'part 2 - {part2}')