import unittest
from _2021.day07.treachery_of_whales import treachery_of_whales

class TestTreachery(unittest.TestCase):

    def test_treachery_of_whales1(self):
        result = treachery_of_whales('test_input.txt')
        self.assertEqual(result, 37)

    def test_treachery_of_whales2(self):
        result = treachery_of_whales('test_input.txt', True)
        self.assertEqual(result, 168)