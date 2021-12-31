from unittest import TestCase
from _2021.day22.reactor_reboot import *


class TestReactorReboot(TestCase):

    def test_extract_reboot_steps(self):
        reboot_step_string = "on x=10..12,y=10..12,z=10..12"
        result = extract_reboot_steps(reboot_step_string)
        self.assertEqual(result, ('on', [10, 12, 1], [10, 12, 1], [10, 12, 1]))

    def test_get_reboot_steps(self):
        result = list(get_reboot_steps('test_input.txt'))
        self.assertEqual(result[0], ('on', [-20, 26, 1], [-36, 17, 1], [-47, 7, 1]))

    def test_part1(self):
        result = part1('test_input2.txt')
        self.assertEqual(result, 39)

    def test_part1_2(self):
        result = part1('test_input.txt')
        self.assertEqual(result, 590784)

    def test_part1_3(self):
        result = part1('test_input3.txt')
        self.assertEqual(result, 210918)

    def test_volume1(self):
        coordinates = ([10, 12, 1], [10, 12, 1], [10, 12, 1])
        self.assertEqual(calculate_volume(*coordinates), 8)

    def test_volume2(self):
        coordinates = ([-20, 26, 1], [-36, 17, 1], [-47, 7, 1])
        self.assertEqual(calculate_volume(*coordinates), 131652)

    def test_not_contains(self):
        a = RectangularPrism((10, 12), (10, 12), (10, 12))
        b = RectangularPrism((11, 13), (11, 13), (11, 13))
        self.assertEqual(a in b, False)

    def test_contains(self):
        a = RectangularPrism((10, 12), (10, 12), (10, 12))
        b = RectangularPrism((11, 12), (11, 12), (11, 12))
        self.assertEqual(a in b, False)
        self.assertEqual(b in a, True)

    def test_intersect(self):
        a = RectangularPrism((10, 12), (10, 12), (10, 12))
        b = RectangularPrism((11, 13), (11, 13), (11, 13))
        self.assertEqual(b.intersect(a), True)

    def test_not_intersect(self):
        a = RectangularPrism((10, 11), (10, 11), (11, 12))
        b = RectangularPrism((9, 12), (9, 12), (9,12))
        self.assertEqual(b.intersect(a), True)

    def test_volume(self):
        a = RectangularPrism((10, 12), (10, 12), (10, 12))
        self.assertEqual(a.volume(), 8)

    def test_part2_small_set(self):
        self.assertEqual(part2('test_input2.txt'), 39)

    def test_part2_regular_set(self):
        self.assertEqual(part2('test_input4.txt'), 2758514936282235)
