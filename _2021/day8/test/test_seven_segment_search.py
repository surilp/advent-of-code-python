import unittest
from _2021.day8.seven_segment_search import SevenSegmentSearch

class TestSevenSegmentSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.seven_segment_search = SevenSegmentSearch('test_input.txt')

    def test_1(self):
        result = self.seven_segment_search.part1()
        self.assertEqual(result, 26)


    def test_2(self):
        result = self.seven_segment_search.part2()
        self.assertEqual(result, 61229)