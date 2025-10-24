from collections import defaultdict
from itertools import count
from pathlib import Path


type Grid = tuple[tuple[int, ...], ...]


def read_notes(notes) -> Grid:
    if Path(notes).exists():
        notes = Path(notes).read_text()
    rows = [
        [int(x) for x in line.split()]
        for line in notes.splitlines()
    ]
    return tuple(
        tuple(column)
        for column in zip(*rows)
    )


def dance(dancers: Grid, round_number: int) -> Grid:
    mutable = [
        list(column)
        for column in dancers
    ]
    clapper = mutable[round_number % 4].pop(0)
    absorb_column = mutable[(round_number + 1) % 4]
    absorptions = list(range(len(absorb_column)))
    absorptions.extend([x + 1 for x in absorptions[::-1]])
    absorb_column.insert(absorptions[(clapper - 1) % len(absorptions)], clapper)
    return tuple(
        tuple(column)
        for column in mutable
    )


def part1(notes: str):
    dancers = read_notes(notes)
    for i in range(10):
        dancers = dance(dancers, i)
    return ''.join(str(column[0]) for column in dancers)


def part2(notes: str) -> int:
    history: dict[int, int] = defaultdict(int)
    dancers = read_notes(notes)
    for round_number in count():
        dancers = dance(dancers, round_number)
        shouted_number = int(''.join(str(column[0]) for column in dancers))
        history[shouted_number] += 1
        if history[shouted_number] == 2024:
            return (round_number + 1) * shouted_number
    return -1  # Technically unreachable


def part3(notes: str) -> int:
    seen_states: set[tuple[Grid, int]] = set()
    highest: int = 0
    dancers = read_notes(notes)
    for round_number in count():
        dancers = dance(dancers, round_number)
        shouted_number = int(''.join(str(column[0]) for column in dancers))
        highest = max(highest, shouted_number)
        state = dancers, round_number % 4
        if state in seen_states:
            break
        seen_states.add(state)
    return highest


if __name__ == '__main__':
    print(part1('inputs/everybody_codes_e2024_q05_p1.txt'))
    print(part2('inputs/everybody_codes_e2024_q05_p2.txt'))
    print(part3('inputs/everybody_codes_e2024_q05_p3.txt'))
