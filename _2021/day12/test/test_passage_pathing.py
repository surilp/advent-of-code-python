from unittest import TestCase
from _2021.day12.passage_pathing import PassagePathing

class TestPassagePathing(TestCase):

    def setUp(self) -> None:
        self.passage_pathing = PassagePathing('test_input.txt')
        self.passage_pathing2 = PassagePathing('test_input2.txt')
        self.passage_pathing3 = PassagePathing('test_input3.txt')

    def test1(self):
        self.assertEqual(self.passage_pathing.part1(), 10)

    def test2(self):
        self.assertEqual(self.passage_pathing.part2(), 36)

    def test3(self):
        self.assertEqual(self.passage_pathing2.part1(), 19)

    def test4(self):
        self.assertEqual(self.passage_pathing2.part2(), 103)

    def test5(self):
        self.assertEqual(self.passage_pathing3.part1(), 226)

    def test6(self):
        self.assertEqual(self.passage_pathing3.part2(), 3509)