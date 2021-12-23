from unittest import TestCase
from _2021.day20.trench_map import part1

class TestTrenchMap(TestCase):

    def test1(self):
        result = part1('test_input.txt', 2)
        self.assertEqual(result, 35)

    def test2(self):
        result = part1('test_input.txt', 50)
        self.assertEqual(result, 3351)