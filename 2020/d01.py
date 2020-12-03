#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/1
"""


def find_2sum(numbers: list[int], searched: int) -> tuple[int, int]:
    seen = set()
    for x in numbers:
        y = searched - x
        if y in seen:
            return x, y
        else:
            seen.add(x)
    return 0, 0


def part1(amounts: list[int]) -> int:
    x, y = find_2sum(amounts, 2020)
    return x * y


def part2(amounts: list[int]) -> int:
    for z in amounts:
        x, y = find_2sum(amounts, 2020 - z)
        if x and y and z:
            return x * y * z


def main():
    input_txt = utils.get_input(1)
    amounts = utils.ints(input_txt)
    print(part1(amounts))
    print(part2(amounts))


if __name__ == "__main__":
    main()
