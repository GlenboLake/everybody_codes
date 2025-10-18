import pytest

from kingdom_of_algorithmia import quest02


@pytest.mark.parametrize('sample, expected', [
    ('AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE', 4),
    ('THE FLAME SHIELDED THE HEART OF THE KINGS', 3),
    ('POWE PO WER P OWE R', 2),
    ('THERE IS THE END', 3),
])
def test_part1(sample, expected):
    words = ['THE', 'OWE', 'MES', 'ROD', 'HER']

    assert quest02.part1(words, sample) == expected


def test_part2():
    words = ['THE', 'OWE', 'MES', 'ROD', 'HER', 'QAQ']
    text = '''AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ'''
    assert quest02.part2(words, text) == 42
