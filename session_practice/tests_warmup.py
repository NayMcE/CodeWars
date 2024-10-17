from unittest import TestCase
from strings import string

class TestAddDashToWord(TestCase):
    
    def test_normal_string(self):
        result = string('Sally')
        self.assertEqual(result, "S-a-l-l-y")

