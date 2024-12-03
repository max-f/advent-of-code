#!/usr/bin/env python

from utils import utils
import re

"""
Code for https://adventofcode.com/2024/day/3
"""


def part1(line: str) -> int:
    print(line)
    total = 0
    result = re.finditer(r"mul\((\d+),(\d+)\)", line)
    for hit in result:
        number1 = hit.group(1)
        number2 = hit.group(2)
        total += int(number1) * int(number2)

    return total


def part2(line: str) -> int:
    result = re.finditer(r"mul\((\d+),(\d+)\)", line)
    mul_statements = []
    for hit in result:
        number1 = hit.group(1)
        number2 = hit.group(2)
        print(number1, number2)
        print(hit.start(0))
        mul_statements.append((int(number1) * int(number2), hit.start(0)))
    dos = [m.start(0) for m in re.finditer(r"do\(\)", line)]
    donts = [m.start(0) for m in re.finditer(r"don't\(\)", line)]


    print(donts)
    print(mul_statements)
    total = 0
    for n, idx in mul_statements:
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
