from _2021.day06.lanternfish import Lanternfish
import unittest

class TestLanternfish(unittest.TestCase):

    def setUp(self) -> None:
        self.lanternfish = Lanternfish('test_input.txt')

    def test1_part1(self):
        self.assertEqual(self.lanternfish.get_result(80), 5934)

    def test2_part1(self):
        self.assertEqual(self.lanternfish.get_result(18), 26)

    def test3_part1(self):
        self.assertEqual(self.lanternfish.get_result(256), 26984457539)



