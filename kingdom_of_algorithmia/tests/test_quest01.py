from kingdom_of_algorithmia import quest01
import pytest


@pytest.mark.parametrize('input, part, expected', [
    pytest.param('ABBAC', 1, 5, id='part 1'),
    pytest.param('AxBCDDCAxD', 2, 28, id='part 2'),
    pytest.param('xBxAAABCDxCC', 3, 30, id='part 3'),
])
def test_quest01(input, part, expected):
    assert quest01.battle(input, part) == expected
