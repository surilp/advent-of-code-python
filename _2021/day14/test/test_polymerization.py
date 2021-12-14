from unittest import TestCase
from _2021.day14.polymerization import Polymerization

class TestPolymerization(TestCase):

    def test1(self):
        p = Polymerization('test_input.txt')
        self.assertEqual(p.final_result(), 1588)

    def test2(self):
        p = Polymerization('test_input.txt')
        self.assertEqual(p.final_result(40), 1588)