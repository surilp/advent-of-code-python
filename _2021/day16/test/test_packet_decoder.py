from unittest import TestCase
from _2021.day16.packet_decoder import PacketDecoder, Packet
from collections import  deque

class TestPacketDecoder(TestCase):



    def test_packet_literal(self):
        packet = Packet("D2FE28", [0], deque())
        self.assertEqual(len(packet.sub_packets), 0)

    def test_packet_15(self):
        packet = Packet("38006F45291200", [0], deque())
        self.assertEqual(len(packet.sub_packets), 2)

    def test_packet_11(self):
        packet = Packet("EE00D40C823060", [0], deque())
        self.assertEqual(len(packet.sub_packets), 3)

    def test_sum_version_3(self):
        packet = PacketDecoder('test_input.txt')
        self.assertEqual(packet.get_version_sum(3), 16)

    def test_sum_version_4(self):
        packet2 = PacketDecoder('test_input.txt')
        self.assertEqual(packet2.get_version_sum(4), 12)

    def test_sum_version_5(self):
        packet = PacketDecoder('test_input.txt')
        self.assertEqual(packet.get_version_sum(5), 23)

    def test_sum_version_6(self):
        packet = PacketDecoder('test_input.txt')
        self.assertEqual(packet.get_version_sum(6), 31)

    def test_part2_sum(self):
        packet = Packet("C200B40A82", [0], deque())
        self.assertEqual(packet.literal_value, 3)

    def test_part2_mult(self):
        packet = Packet("04005AC33890", [0], deque())
        self.assertEqual(packet.literal_value, 54)

    def test_part2_min(self):
        packet = Packet("880086C3E88112", [0], deque())
        self.assertEqual(packet.literal_value, 7)

    def test_part2_max(self):
        packet = Packet("CE00C43D881120", [0], deque())
        self.assertEqual(packet.literal_value, 9)

    def test_part2_greater(self):
        packet = Packet("D8005AC2A8F0", [0], deque())
        self.assertEqual(packet.literal_value, 1)

    def test_part2_less(self):
        packet = Packet("F600BC2D8F", [0], deque())
        self.assertEqual(packet.literal_value, 0)

    def test_part2_equal(self):
        packet = Packet("9C005AC2F8F0", [0], deque())
        self.assertEqual(packet.literal_value, 0)

    def test_part2_final(self):
        packet = Packet("9C0141080250320F1802104A08", [0], deque())
        self.assertEqual(packet.literal_value, 1)