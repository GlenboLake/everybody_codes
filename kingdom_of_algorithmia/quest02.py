import re


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
    text = text.splitlines()
    width = len(text[0])
    transposed = [
        ''.join(z)
        for z in zip(*text)
    ]
    text = [line*2 for line in text]

    def locations(s: str, grid: list[str]):
        for r, line in enumerate(grid):
            i = 0
            while (c := line.find(s, i)) >= 0:
                yield r, c
                i = c + 1

    runic = set()
    for word in words:
        for start_r, start_c in locations(word, text):
            if start_c >= width:
                continue
            points = [(start_r, start_c + i) for i in range(len(word))]
            runic.update(points)
        for start_r, start_c in locations(word[::-1], text):
            if start_c >= width:
                continue
            points = [(start_r, start_c + i) for i in range(len(word))]
            runic.update(points)
        for start_c, start_r in locations(word, transposed):
            if start_r >= width:
                continue
            points = [(start_r + i, start_c) for i in range(len(word))]
            runic.update(points)
        for start_c, start_r in locations(word[::-1], transposed):
            if start_r >= width:
                continue
            points = [(start_r + i, start_c) for i in range(len(word))]
            runic.update(points)

    runic = {(r, c % width) for r, c in runic}

    return len(runic)


if __name__ == '__main__':
    print(part1(*read_input('inputs/everybody_codes_e2024_q02_p1.txt')))
    print(part2(*read_input('inputs/everybody_codes_e2024_q02_p2.txt')))
    print(part3(*read_input('inputs/everybody_codes_e2024_q02_p3.txt')))
