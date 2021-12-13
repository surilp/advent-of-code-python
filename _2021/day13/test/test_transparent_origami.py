from unittest import TestCase
from _2021.day13.transparent_origami import TransparentOrigami


class TestTransparentOrigami(TestCase):

    def test1(self):
        t = TransparentOrigami('test_input.txt')
        self.assertEqual(t.part1(), 17)

    def test2(self):
        t = TransparentOrigami('test_input.txt')
        self.assertEqual(t.part2(), 16)
