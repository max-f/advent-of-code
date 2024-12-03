#!/usr/bin/env python

from utils import utils
import re

"""
Code for https://adventofcode.com/2024/day/3
"""


MULTIPLY_PATTERN = r"mul\((\d+),(\d+)\)"
DO_PATTERN = r"do\(\)"
DONT_PATTERN = r"don't\(\)"


def part1(line: str) -> int:
    matches = re.finditer(MULTIPLY_PATTERN, line)
    return sum([int(mul.group(1)) * int(mul.group(2)) for mul in matches])


def part2(line: str) -> int:
    matches = re.finditer(MULTIPLY_PATTERN, line)
    muls = [(int(mul.group(1)) * int(mul.group(2)), mul.start(0)) for mul in matches]
    dos = [m.start(0) for m in re.finditer(DO_PATTERN, line)]
    donts = [m.start(0) for m in re.finditer(DONT_PATTERN, line)]

    total = 0
    for n, idx in muls:
        closest_do = max((d for d in dos if d < idx), default=-1)
        closest_dont = max((d for d in donts if d < idx), default=-1)
        if closest_dont > closest_do:
            continue
        total += n
    return total


def main():
    input_txt = utils.get_input(3)
    print(f"Part1: {part1(input_txt)}")
    print(f"Part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
