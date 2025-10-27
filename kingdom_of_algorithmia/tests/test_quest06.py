from textwrap import dedent

from kingdom_of_algorithmia import quest06


def test_part1():
    notes = dedent('''\
        RR:A,B,C
        A:D,E
        B:F,@
        C:G,H
        D:@
        E:@
        F:@
        G:@
        H:@
    ''')
    assert quest06.part1(notes) == 'RRB@'


def test_part2():
    notes = dedent('''\
        RR:AAAAA,BBBBB,CCCCC
        AAAAA:DDDDD,EEEEE
        BBBBB:FFFFF,@
        CCCCC:GGGGG,HHHHH
        DDDDD:@
        EEEEE:@
        FFFFF:@
        GGGGG:@
        HHHHH:@
    ''')
    assert quest06.part2(notes) == 'RB@'