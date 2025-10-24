from statistics import median
from typing import Collection


def parse(filename):
    with open(filename) as f:
        return [int(line) for line in f]


def part1_2(nums: Collection[int]):
    return sum(nums) - min(nums) * len(nums)


def part3(nums: Collection[int]):
    target = int(median(nums))
    return sum(abs(n-target) for n in nums)


if __name__ == '__main__':
    print(part1_2(parse('inputs/everybody_codes_e2024_q04_p1.txt')))
    print(part1_2(parse('inputs/everybody_codes_e2024_q04_p2.txt')))
    print(part3(parse('inputs/everybody_codes_e2024_q04_p3.txt')))
