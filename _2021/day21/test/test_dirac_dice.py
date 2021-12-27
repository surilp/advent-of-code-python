from unittest import TestCase
from _2021.day21.dirac_dice import *

class TestDiracDice(TestCase):

    def test_extract_player_position(self):
        p1_position, p2_position = extract_player_positions('test_input.txt')
        self.assertEqual(p1_position, 4)
        self.assertEqual(p2_position, 8)

    def test_location_update(self):
        self.assertEqual(location_update_and_score(4, 6, 0),(10,10))
        self.assertEqual(location_update_and_score(10, 7+8+9, 10),(4,14))

    def test_play_game_part1(self):
        self.assertEqual(play_game_part1('test_input.txt'), 739785)

    def test_play_game_part1(self):
        self.assertEqual(play_game_part2('test_input.txt'), (444356092776315, 341960390180808))