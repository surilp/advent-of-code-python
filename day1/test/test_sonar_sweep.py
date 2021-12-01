import unittest
from day1.sonar_sweep import sonar_sweep, window_sonar_sweep

class SonarSweep(unittest.TestCase):

    def test_sonar_sweep(self):
        result = sonar_sweep('test_input.txt')
        self.assertEqual(result, 7)

    def test_window_sonar_sweep(self):
        result = window_sonar_sweep('test_input.txt')
        self.assertEqual(result, 5)
