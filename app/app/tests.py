"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(4,6)

        self.assertEqual(res, 10)

    def test_add_numbers_negative(self):
        """Test adding numbers with negatives"""
        res = calc.add(4,-6)

        self.assertEqual(res, -2)
        