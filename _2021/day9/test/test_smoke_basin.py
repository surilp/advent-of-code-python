from _2021.day9.smoke_basin import part1_result, part2_result
import unittest

class TestSmokeBasin(unittest.TestCase):

    def test1(self):
        self.assertEqual(part1_result('test_input.txt'), 15)

    def test2(self):
        self.assertEqual(part2_result('test_input.txt'), 1134)