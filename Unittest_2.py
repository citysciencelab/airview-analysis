import unittest
from General_statistics import negative_per
from measurement_list import data_without_outliers

# Functions to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

data = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# Test class
class TestMathOperations(unittest.TestCase):

    def negative_value_count(self):
        #self.assertEqual(negative_per(data), 10)
        self.assertEqual(data_without_outliers(data, 1, 7), [1, 2, 3, 4, 5, 6, 7, 8, 10])
        self.assertEqual(add(-3, -5), -8)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(-5, -3), -2)

if __name__ == '__main__':
    unittest.main()
