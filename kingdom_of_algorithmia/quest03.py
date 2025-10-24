from collections import defaultdict, deque
from pathlib import Path
from typing import Callable

type Point = tuple[int, int]


def cardinal(point: Point) -> list[Point]:
    r, c = point
    return [
        (r, c + 1),
        (r, c - 1),
        (r + 1, c),
        (r - 1, c),
    ]


def diagonal(point: Point) -> list[Point]:
    r, c = point
    return [
        *cardinal(point),
        (r + 1, c + 1),
        (r - 1, c - 1),
        (r + 1, c - 1),
        (r - 1, c + 1),
    ]


def part1_2(notes):
    return dig(notes, cardinal)


def part3(notes):
    # Pad the text!
    lines = notes.splitlines()
    line_length = len(lines[0])
    padded = '\n'.join([
        '.' * (line_length+2),
        *[
            '.' + line + '.'
            for line in lines
        ],
        '.' * (line_length+2),
    ])
    return dig(padded, diagonal)


def dig(notes: str, adjacency: Callable[[Point], list[Point]]):
    to_dig = set()
    plot = dict()
    for r, row in enumerate(notes.splitlines()):
        for c, ch in enumerate(row):
            if ch == '#':
                to_dig.add((r, c))
            else:
                plot[r, c] = 0

    def adjacent_to(point: tuple[int, int], value: int) -> bool:
        nonlocal plot
        return any(plot.get(n) == value for n in adjacency(point))

    def print_plot():
        nonlocal plot
        for rr in range(len(notes.splitlines())):
            for cc in range(notes.index('\n')):
                print(plot.get((rr, cc), '#') or '.', end='')
            print()

    check = 0
    while to_dig:
        diggable = {
            p for p in to_dig
            if adjacent_to(p, check)
        }
        check += 1
        for d in diggable:
            plot[d] = check
        to_dig -= diggable

    return sum(plot.values())


if __name__ == '__main__':
    print(part1_2(Path('inputs/everybody_codes_e2024_q03_p1.txt').read_text()))
    print(part1_2(Path('inputs/everybody_codes_e2024_q03_p2.txt').read_text()))
    print(part3(Path('inputs/everybody_codes_e2024_q03_p3.txt').read_text()))
