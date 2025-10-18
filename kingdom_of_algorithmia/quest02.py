import re
from typing import Iterable


def read_input(filename: str) -> tuple[list[str], str]:
    with open(filename) as f:
        key, text = f.read().strip().split('\n\n')
        words = key.split(':')[-1].split(',')
    return words, text


def part1(words: list[str], text: str) -> int:
    return sum(
        text.count(word)
        for word in words
    )


def part2(words: list[str], text: str) -> int:
    runic = set()
    for word in words:
        for match in re.finditer(fr'(?={word}|{word[::-1]})', text):
            runic.update(range(match.start(), match.start() + len(word)))
    return len(runic)


def part3(words: list[str], text: str) -> int:
    type Point = tuple[int, int]

    RIGHT: Point = 0, 1
    LEFT: Point = 0, -1
    UP: Point = -1, 0
    DOWN: Point = 1, 0

    lines = text.splitlines()
    width = len(lines[0])

    def check(word: str, pos: Point, d: Point) -> Iterable[Point]:
        r, c = pos
        dr, dc = d
        checks = [(letter, (r + i * dr, (c + i * dc) % width)) for i, letter in enumerate(word)]
        for letter, (row, col) in checks:
            if row < 0:
                # Can't go above the first row, but Python will try to wrap with negative indices
                return ()
            try:
                if lines[row][col] != letter:
                    return ()
            except IndexError:
                return ()
        return {p for _, p in checks}

    points = set()
    for row, line in enumerate(lines):
        for col, _ in enumerate(line):
            for word in words:
                for dir_ in LEFT, RIGHT, UP, DOWN:
                    points.update(check(word, (row, col), dir_))
    return len(points)


if __name__ == '__main__':
    print(part1(*read_input('everybody_codes_e2024_q02_p1.txt')))
    print(part2(*read_input('everybody_codes_e2024_q02_p2.txt')))
    print(part3(*read_input('everybody_codes_e2024_q02_p3.txt')))
