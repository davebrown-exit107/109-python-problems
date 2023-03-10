import pytest

from .main import colour_trio

def test_colour_trio():
    test_cases = {
            'y': 'y',
            'bb': 'b',
            'rybyry': 'r',
            'brybbr': 'r',
            'rbyryrrbyrbb': 'y',
            'yrbbbbryyrybb': 'b'}

    for n, expected in test_cases.items():
        assert(colour_trio(n) == expected)
