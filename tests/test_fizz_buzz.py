import pytest

from src.fizz_buzz import fizz_buzz


def test_divisible_by_3():
    """
    Test if is divisible with 4
    """
    assert fizz_buzz(3) == 'fizz'


def test_divisible_by_5():
    """
    Test if is divisible by 5
    """
    assert fizz_buzz(5) == 'buzz'

def test_divisible_by_5_and_3():
    """
    Test if is divisible by 5 and 3
    """
    assert fizz_buzz(3*5) == 'fizzbuzz'