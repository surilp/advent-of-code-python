from unittest import TestCase
from _2021.day14.polymerization import Polymerization, part2

class TestPolymerization(TestCase):

    def test1(self):
        p = Polymerization('test_input.txt')
        self.assertEqual(p.final_result(), 1588)

    def test2(self):
        self.assertEqual(part2('test_input.txt', 10), 1588)