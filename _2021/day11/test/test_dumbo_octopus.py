import unittest
from _2021.day11.dumbo_octopus import DumboOctopus


class TestDumboOctopus(unittest.TestCase):

    def setUp(self) -> None:
        self.oct = DumboOctopus('test_input2.txt')
        self.oct2 = DumboOctopus('test_input.txt')

    def test1(self):
        result = self.oct.part1(1)
        self.assertEqual(
            self.oct.grid,
            [[3, 4, 5, 4, 3], [4, 0, 0, 0, 4], [5, 0, 0, 0, 5], [4, 0, 0, 0, 4], [3, 4, 5, 4, 3]]
        )
        self.assertEqual(result, 9)

    def test2(self):
        result = self.oct.part1(2)
        self.assertEqual(
            self.oct.grid,
            [[4, 5, 6, 5, 4], [5, 1, 1, 1, 5], [6, 1, 1, 1, 6], [5, 1, 1, 1, 5], [4, 5, 6, 5, 4]]
        )
        self.assertEqual(result, 9)

    def test3(self):
        result = self.oct2.part1(10)
        self.assertEqual(result, 204)

    def test4(self):
        result = self.oct2.part1(100)
        self.assertEqual(result, 1656)

    def test5(self):
        result = self.oct2.part2()
        self.assertEqual(result, 195)
