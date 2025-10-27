from collections import Counter
from collections.abc import Collection, Generator, Iterable
from pathlib import Path

type Roots = dict[str, Iterable[str]]


def parse_notes(notes: str) -> Roots:
    if Path(notes).exists():
        notes = Path(notes).read_text()

    def parse_line(line):
        a, b = line.split(':')
        return a, b.split(',')

    return dict(map(parse_line, notes.splitlines()))


def iter_paths(root_system: Roots) -> Generator[Collection[str], None, None]:
    paths: list[tuple[str, ...]] = [('RR',)]
    while paths:
        path = paths.pop()
        if path[-1] == '@':
            yield path
            continue
        if path[-1] not in root_system:
            continue
        next_roots = root_system[path[-1]]
        paths.extend([
            (*path, nr)
            for nr in next_roots
        ])


def part1(notes: str) -> str:
    roots: Roots = parse_notes(notes)
    all_roots = list(iter_paths(roots))
    length_frequency = Counter(len(r) for r in all_roots)
    best = next(k for k, v in length_frequency.items() if v == 1)
    path = next(root for root in all_roots if len(root) == best)
    return ''.join(path)


def part2(notes: str) -> str:
    roots: Roots = parse_notes(notes)
    all_roots = list(iter_paths(roots))
    length_frequency = Counter(len(r) for r in all_roots)
    best = next(k for k, v in length_frequency.items() if v == 1)
    path = next(root for root in all_roots if len(root) == best)
    return ''.join(node[0] for node in path)


def part3(notes: str) -> str:
    roots: Roots = parse_notes(notes)
    del roots['BUG']
    del roots['ANT']
    all_roots = list(iter_paths(roots))
    length_frequency = Counter(len(r) for r in all_roots)
    best = next(k for k, v in length_frequency.items() if v == 1)
    path = next(root for root in all_roots if len(root) == best)
    return ''.join(node[0] for node in path)


if __name__ == '__main__':
    print(part1('inputs/everybody_codes_e2024_q06_p1.txt'))
    print(part2('inputs/everybody_codes_e2024_q06_p2.txt'))
    print(part3('inputs/everybody_codes_e2024_q06_p3.txt'))
