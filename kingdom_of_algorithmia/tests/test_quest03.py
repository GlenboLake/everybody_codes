from kingdom_of_algorithmia import quest03

sample_input = '''\
    ..........
    ..###.##..
    ...####...
    ..######..
    ..######..
    ...####...
    ..........
'''

def test_part1():
    assert quest03.part1_2(sample_input) == 35

def test_part3():
    assert quest03.part3(sample_input) == 29