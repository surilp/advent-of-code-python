from unittest import TestCase
from _2021.day19.beacon_scanner import part1, taxicab_distance,largest_taxicab_distance

class TestBeaconScanner(TestCase):


    def test_part1_part2(self):
        num_of_beacons, scanner_location = part1('test_input.txt')
        self.assertEqual(num_of_beacons, 79)
        max_taxi_cab_distance = largest_taxicab_distance(scanner_location)
        self.assertEqual(max_taxi_cab_distance, 3621)

    def test_taxi_cab(self):
        scanner1 = (1105,-1205,1229)
        scanner2 = (-92,-2380,-20)
        result = taxicab_distance(scanner1, scanner2)
        self.assertEqual(result, 3621)