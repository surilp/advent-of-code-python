import unittest
from _2021.day02.dive import dive, dive2

class TestDive(unittest.TestCase):

    def test_dive(self):
        result = dive('test_input.txt')
        self.assertEqual(result, 150)

    def test_dive2(self):
        result = dive2('test_input.txt')
        self.assertEqual(result, 900)