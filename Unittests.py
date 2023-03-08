import unittest
from functions import calculate_statistics

class TestCalculateStatistics(unittest.TestCase):

    def test_calculate_statistics(self):
        # Test case 1: Test with valid input data
        data = {"field1": [1, 2, 3, 4, 5]}
        expected_output = {"mean": 3.0, "median": 3.0, "25th percentile": 2.0, "75th percentile": 4.0}
        self.assertDictEqual(calculate_statistics(data), expected_output)

        # Test case 2: Test with empty input data
        data = {"field1": []}
        expected_output = {"mean": None, "median": None, "25th percentile": None, "75th percentile": None}
        self.assertDictEqual(calculate_statistics(data), expected_output)

        # Test case 3: Test with invalid input data
        data = {"field1": "invalid data"}
        with self.assertRaises(TypeError):
            calculate_statistics(data)

