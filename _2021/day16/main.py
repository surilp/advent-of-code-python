from packet_decoder import PacketDecoder


packetDecoder = PacketDecoder('input.txt')

part1 = packetDecoder.get_version_sum()
part2 = packetDecoder.packet_literal_value()


print(f'part 1 - {part1}')
print(f'part 2 - {part2}')