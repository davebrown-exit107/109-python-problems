import pytest

from .main import only_odd_digits

def test_only_odd_digits():
    test_cases = {
            8: False,
            1357975313579: True,
            42: False,
            71358: False,
            0: False}

    for n, expected in test_cases.items():
        assert(only_odd_digits(n) == expected)
