import unittest
from _2021.day05.hydrothermal_venture import HydrothermalVenture


class TestHydrothermalVenture(unittest.TestCase):

    def setUp(self) -> None:
        self.hydrothermal_venture = HydrothermalVenture('test_input.txt')

    def test_part1(self):
        self.assertEqual(self.hydrothermal_venture.get_part1_result(), 5)

    def test_part2(self):
        self.assertEqual(self.hydrothermal_venture.get_part2_result(), 12)