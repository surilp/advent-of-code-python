import unittest
from _2021.day3.binary_diagnostic import binary_diagnostic, binary_diagnostic2

class TestBinaryDiagnostic(unittest.TestCase):

    def test_binary_diagnostic(self):
        result = binary_diagnostic('test_input.txt')
        self.assertEqual(result, 198)

    def test_binary_diagnostic2(self):
        result = binary_diagnostic2('test_input.txt')
        self.assertEqual(result, 230)
