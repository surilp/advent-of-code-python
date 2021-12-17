from unittest import TestCase
from _2021.day17.trick_shot import TrickShot

class TestTrickShot(TestCase):

    def test1(self):
        max_y = TrickShot('test_input.txt').part1()
        self.assertEqual(max_y, 45)

    def test2(self):
        total = TrickShot('test_input.txt').part2()
        self.assertEqual(total, 112)