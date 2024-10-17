from unittest import TestCase
from strings import string

class TestAddDashToWord(TestCase):
    
    def test_normal_string(self):
        result = string('Sally')
        expected_result = "S-a-l-l-yyyyyyy"
        self.assertEqual(result, expected_result)

