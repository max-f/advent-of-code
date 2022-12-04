#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/4
"""


def part1(lines: list[str]) -> int:
    score = 0
    for line in lines:
        (b11, b12, b21, b22) = utils.positive_ints(line)
        if (b11 <= b21 and b12 >= b22) or (b21 <= b11 and b22 >= b12):
            score += 1
    return score


def part2(lines: list[str]) -> int:
    score = 0
    for line in lines:
        (b11, b12, b21, b22) = utils.positive_ints(line)
        if (b11 <= b21 <= b12) or (b21 <= b11 <= b22):
            score += 1
    return score


def main():
    input_txt = utils.get_input(4)
    lines = [line for line in input_txt.split("\n") if line.strip()]

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
