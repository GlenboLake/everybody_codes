from textwrap import dedent

import pytest

from kingdom_of_algorithmia.quest05 import *


def test_read_notes():
    notes = dedent('''\
        2 3 4 5
        3 4 5 2
        4 5 2 3
        5 2 3 4
    ''')
    expected = [
        [2, 3, 4, 5],
        [3, 4, 5, 2],
        [4, 5, 2, 3],
        [5, 2, 3, 4],
    ]
    assert read_notes(notes) == expected


@pytest.mark.parametrize('dancers, round_number, expected', [
    ([[2, 3, 4, 5], [3, 4, 5, 2], [4, 5, 2, 3], [5, 2, 3, 4]], 0, [[3, 4, 5], [3, 2, 4, 5, 2], [4, 5, 2, 3], [5, 2, 3, 4]]),
    ([[3, 4, 5], [3, 2, 4, 5, 2], [4, 5, 2, 3], [5, 2, 3, 4]], 1, [[3, 4, 5], [2, 4, 5, 2], [4, 5, 3, 2, 3], [5, 2, 3, 4]]),
    ([[3, 4, 5], [2, 4, 5, 2], [4, 5, 3, 2, 3], [5, 2, 3, 4]], 2, [[3, 4, 5], [2, 4, 5, 2], [5, 3, 2, 3], [5, 2, 3, 4, 4]]),
    ([[3, 4, 5], [2, 4, 5, 2], [5, 3, 2, 3], [5, 2, 3, 4, 4]], 3, [[3, 4, 5, 5], [2, 4, 5, 2], [5, 3, 2, 3], [2, 3, 4, 4]]),
])
def test_dance(dancers, round_number, expected):
    assert dance(dancers, round_number) == expected


def test_part1():
    sample_notes = dedent('''\
        2 3 4 5
        3 4 5 2
        4 5 2 3
        5 2 3 4
    ''')
    assert part1(sample_notes) == '2323'


def test_part2():
    sample_notes = dedent('''\
        2 3 4 5
        6 7 8 9
    ''')
    assert part2(sample_notes) == 50877075


def test_part3():
    sample_notes = dedent('''\
        2 3 4 5
        6 7 8 9
    ''')
    assert part3(sample_notes) == 6584
