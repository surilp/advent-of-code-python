from unittest import TestCase
from _2021.day18.snail_fish import SnailFish


class TestSnailFish(TestCase):

    def test_explode_1(self):
        number = [[[[[9, 8], 1], 2], 3], 4]
        SnailFish.explode_split_snail_fish_number(number)
        self.assertEqual(number, [[[[0, 9], 2], 3], 4])

    def test_explode_2(self):
        number = [7, [6, [5, [4, [3, 2]]]]]
        SnailFish.explode_split_snail_fish_number(number)
        self.assertEqual(number, [7, [6, [5, [7, 0]]]])

    def test_explode_3(self):
        number = [[6, [5, [4, [3, 2]]]], 1]
        SnailFish.explode_split_snail_fish_number(number)
        self.assertEqual(number, [[6, [5, [7, 0]]], 3])

    def test_explode_4(self):
        number = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
        SnailFish.explode_split_snail_fish_number(number)
        self.assertEqual(number, [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])

    def test_explode_5(self):
        number = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
        SnailFish.explode_split_snail_fish_number(number)
        self.assertEqual(number, [[3, [2, [8, 0]]], [9, [5, [7, 0]]]])

    def test_add_1(self):
        num1 = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
        num2 = [1, 1]
        result = SnailFish.add_snail_Fish_numbers(num1, num2)
        self.assertEqual(result, [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])

    def test_add_2(self):
        numbers = [[1, 1], [2, 2], [3, 3], [4, 4]]
        result = SnailFish.sum_snail_fish_numbers(numbers)
        self.assertEqual(result, [[[[1, 1], [2, 2]], [3, 3]], [4, 4]])

    def test_add_3(self):
        numbers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        result = SnailFish.sum_snail_fish_numbers(numbers)
        self.assertEqual(result, [[[[3, 0], [5, 3]], [4, 4]], [5, 5]])

    def test_add_4(self):
        numbers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
        result = SnailFish.sum_snail_fish_numbers(numbers)
        self.assertEqual(result, [[[[5, 0], [7, 4]], [5, 5]], [6, 6]])

    def test_all_1(self):
        result = SnailFish('test_input.txt').process()
        self.assertEqual(result, [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])

    def test_magnitude1(self):
        result = SnailFish.calculate_magnitude([[1, 2], [[3, 4], 5]])
        self.assertEqual(result, 143)

    def test_magnitude2(self):
        result = SnailFish.calculate_magnitude([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])
        self.assertEqual(result, 445)

    def test_magnitude3(self):
        result = SnailFish.calculate_magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
        self.assertEqual(result, 1384)

    def test_magnitude4(self):
        result = SnailFish.calculate_magnitude([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])
        self.assertEqual(result, 791)

    def test_magnitude5(self):
        result = SnailFish.calculate_magnitude([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])
        self.assertEqual(result, 1137)

    def test_magnitude6(self):
        result = SnailFish.calculate_magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
        self.assertEqual(result, 3488)

    def test_all_magnitude_1(self):
        snail_fish_num_sum = SnailFish('test_input2.txt').process()
        magnitude = SnailFish('test_input2.txt').part1_magnitude()
        self.assertEqual(snail_fish_num_sum, [[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]])
        self.assertEqual(magnitude, 4140)

    def test_max_magnitude_1(self):
        max_magnitude = SnailFish('test_input2.txt').max_magnitude_part2()
        self.assertEqual(max_magnitude, 3993)
