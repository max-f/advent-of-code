#!/usr/bin/env python

from utils import utils
from collections import Counter

"""
Code for https://adventofcode.com/2024/day/1
"""


def part1(numbers1: list[int], numbers2: list[int]) -> int:
    return sum(abs(n1 - n2) for n1, n2 in zip(numbers1, numbers2))


def part2(numbers1: list[int], numbers2: list[int]) -> int:
    n2_counter = Counter(numbers2)
    return sum(n * n2_counter[n] for n in numbers1)


def parse_input(input_txt: str) -> tuple[list[int], list[int]]:
    numbers = [utils.ints(line) for line in input_txt.strip().split("\n")]
    numbers1, numbers2 = zip(*numbers)
    return sorted(numbers1), sorted(numbers2)


def main():
    input_txt = utils.get_input(1)
    numbers1, numbers2 = parse_input(input_txt)

    print(f"Part1: {part1(numbers1, numbers2)}")
    print(f"Part2: {part2(numbers1, numbers2)}")


if __name__ == "__main__":
    main()
