from unittest import TestCase
from _2021.day15.chiton import Chiton, Grid


class TestChiton(TestCase):

    def test1(self):
        c = Chiton('test_input.txt', 1)
        self.assertEqual(c.result(), 40)

    def test2(self):
        c = Chiton('test_input.txt', 5)
        self.assertEqual(c.result(), 315)

    def test_grid(self):
        grid = Grid([
            [8]
        ], 5)
        self.assertEqual(grid[(0, 0)], 8)
        self.assertEqual(grid[(0, 1)], 9)
        self.assertEqual(grid[(0, 2)], 1)
        self.assertEqual(grid[(0, 3)], 2)
        self.assertEqual(grid[(0, 4)], 3)
        self.assertEqual(grid[(1, 0)], 9)
        self.assertEqual(grid[(1, 1)], 1)
        self.assertEqual(grid[(1, 2)], 2)
        self.assertEqual(grid[(1, 3)], 3)
        self.assertEqual(grid[(1, 4)], 4)
        self.assertEqual(grid[(2, 0)], 1)
        self.assertEqual(grid[(2, 1)], 2)
        self.assertEqual(grid[(2, 2)], 3)
        self.assertEqual(grid[(2, 3)], 4)
        self.assertEqual(grid[(2, 4)], 5)
        self.assertEqual(grid[(3, 0)], 2)
        self.assertEqual(grid[(3, 1)], 3)
        self.assertEqual(grid[(3, 2)], 4)
        self.assertEqual(grid[(3, 3)], 5)
        self.assertEqual(grid[(3, 4)], 6)
        self.assertEqual(grid[(4, 0)], 3)
        self.assertEqual(grid[(4, 1)], 4)
        self.assertEqual(grid[(4, 2)], 5)
        self.assertEqual(grid[(4, 3)], 6)
        self.assertEqual(grid[(4, 4)], 7)
