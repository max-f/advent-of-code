#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2021/day/1
"""


def part1(depths: list[int]) -> int:
    increased = 0
    for i, x in enumerate(depths):
        if i > 0 and depths[i - 1] < x:
            increased += 1
    return increased


def part2(depths: list[int]) -> int:
    increased = 0
    for i, x in enumerate(depths[:-3]):
        cur_window = sum(depths[i : i + 3])
        next_window = sum(depths[i + 1 : i + 4])
        if cur_window < next_window:
            increased += 1

    return increased


def main():
    input_txt = utils.get_input(1)
    depths = utils.ints(input_txt)
    print(part1(depths))
    print(part2(depths))


if __name__ == "__main__":
    main()
