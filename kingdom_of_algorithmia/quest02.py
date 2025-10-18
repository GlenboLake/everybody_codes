import re


def read_input(filename):
    with open(filename) as f:
        key, _, *text = f.read().splitlines()
        words = key.split(':')[-1].split(',')
    return words, '\n'.join(text)


def part1(words: list[str], text: str) -> int:
    return sum(
        text.count(word)
        for word in words
    )


def part2(words, text):
    runic = set()
    for word in words:
        for match in re.finditer(fr'(?={word}|{word[::-1]})', text):
            runic.update(range(match.start(), match.start() + len(word)))
    return len(runic)


if __name__ == '__main__':
    print(part1(*read_input('everybody_codes_e2024_q02_p1.txt')))
    print(part2(*read_input('everybody_codes_e2024_q02_p2.txt')))
