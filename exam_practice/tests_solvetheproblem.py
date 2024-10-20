from unittest import TestCase
from solve_the_problem import total_sales

class Testtotalsales(TestCase):
    
    def test_normal_string(self):
        result = total_sales({"apple": 0.5, "banana": 0.3, "orange": 0.7,"grape": 1.2}, {"apple": 10, "banana": 5, "orange": 8, "grape": 12})
        expected_result = 23.5
        self.assertEqual(result, expected_result)

    def test_normal_string(self):
        result = total_sales({"apple": 0, "banana": 0.3, "orange": 0.7,"grape": 1.2}, {"apple": 10, "banana": 5, "orange": 8, "grape": 12})
        expected_result = 23.5
        self.assertEqual(result, expected_result)

    def test_normal_string(self):
        result = total_sales({"apple": 0.5, "banana": 0.3, "orange": 0.7,"grape": 1.2}, {"apple": 0, "banana": 0, "orange": 0, "grape": 0})
        expected_result = 0
        self.assertEqual(result, expected_result)

        