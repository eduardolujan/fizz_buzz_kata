import pytest
import unittest

from src.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3(self):
        """
        Test if is divisible with 4
        """
        self.assertEqual(fizz_buzz(3), 'fizz')

    def test_divisible_by_5(self):
        """
        Test if is divisible by 5
        """
        self.assertEqual(fizz_buzz(5), 'buzz')

    def test_divisible_by_5_and_3(self):
        """
        Test if is divisible by 5 and 3
        """
        self.assertEqual(fizz_buzz(3*5), 'fizzbuzz')