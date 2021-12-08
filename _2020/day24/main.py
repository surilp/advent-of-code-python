from lobby_layout import LobbyLayout

l = LobbyLayout('input.txt')

part1_result = l.run_part1()
part2_result = l.run_part2(100)

print(f'part 1 result - {part1_result}')

print(f'part 2 result - {part2_result}')