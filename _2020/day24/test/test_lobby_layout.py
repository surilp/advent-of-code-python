import unittest
from _2020.day24.lobby_layout import LobbyLayout


class TestLobbyLayout(unittest.TestCase):
    def setUp(self) -> None:
        self.lobby_layout = LobbyLayout('test_input.txt')

    def test_parse1(self):
        result = self.lobby_layout.parse_direction('esenee')
        self.assertEqual(result, ['e', 'se', 'ne', 'e'])

    def test_parse2(self):
        result = self.lobby_layout.parse_direction('sesenwnenenewseeswwswswwnenewsewsw')
        self.assertEqual(result,
                         ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne',
                          'w', 'se', 'w', 'sw'])
    def test_traverse1(self):
        directions = self.lobby_layout.parse_direction('nwwswee')
        result = self.lobby_layout.traverse_directions(directions)
        self.assertEqual(result, (0.0, 0.0))

    def test_part1(self):
        result = self.lobby_layout.run_part1()
        self.assertEqual(result, 10)

    def test_part2(self):
        result = self.lobby_layout.run_part2(100)
        self.assertEqual(result, 2208)