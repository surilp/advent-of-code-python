import unittest
from _2021.day10.syntax_scoring import syntax_scoring


class TestSyntaxScoring(unittest.TestCase):

    def test1(self):
        part1_result, part2_result = syntax_scoring('test_input.txt')
        self.assertEqual(part1_result, 26397)
        self.assertEqual(part2_result, 288957)
