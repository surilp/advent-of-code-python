import unittest
from _2021.day04.giant_squid import GiantSquid

class TestGiantSquid(unittest.TestCase):

    def setUp(self) -> None:
        self.giant_squid = GiantSquid('test_input.txt')

    def test_giant_squid1(self):
        result = self.giant_squid.play_game(True)
        self.assertEqual(result, 4512)

    def test_giant_squid2(self):
        result = self.giant_squid.play_game(False)
        self.assertEqual(result, 1924)