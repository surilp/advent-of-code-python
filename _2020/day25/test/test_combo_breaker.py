import unittest
from _2020.day25.combo_breaker import ComboBreaker

class TestComboBreaker(unittest.TestCase):

    def setUp(self) -> None:
        self.combo_breaker = ComboBreaker('test_input.txt', 7)

    def test1(self):
        result = self.combo_breaker.get_encryption()
        self.assertEqual(result, 14897079)