from itertools import batched
from typing import Iterable

potions = {
    'x': 0,
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
}


def battle_group(foes: Iterable[str]):
    num_foes = sum(1 for foe in foes if foe != 'x')
    cost = sum(potions[foe] for foe in foes)
    extra = num_foes * (num_foes - 1)
    return cost + extra


def battle(foes: Iterable[str], group_size: int):
    return sum(battle_group(group) for group in batched(foes, group_size))


if __name__ == '__main__':
    for part in (1, 2, 3):
        with open(f'inputs/everybody_codes_e2024_q01_p{part}.txt') as f:
            print(f'Part {part}', battle(f.read(), part))
