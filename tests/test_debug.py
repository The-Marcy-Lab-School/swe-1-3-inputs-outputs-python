import pytest

from debug import first_initial, shout, total_with_tax

TEST_SUITE_NAME = "Debug Tests"


def test_total_with_tax():
    """total_with_tax - adds 1 to a price that arrives as text"""
    assert total_with_tax("4") == 5
    assert total_with_tax("0") == 1
    assert total_with_tax("19") == 20


def test_first_initial():
    """first_initial - returns the first letter, capitalized"""
    assert first_initial("ada") == "A"
    assert first_initial("Zo") == "Z"
    assert first_initial("b") == "B"


def test_shout():
    """shout - capitalizes the first letter and adds an exclamation mark"""
    assert shout("hello") == "Hello!"
    assert shout("a") == "A!"
    assert shout("Already") == "Already!"
