#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/6
"""


def part1(buffer: str) -> int:
    marker_size = 4
    for i, window in enumerate(utils.sliding_window(buffer, win_size=marker_size)):
        if len(set(window)) == marker_size:
            return i + marker_size


def part2(buffer: str) -> int:
    marker_size = 14
    for i, window in enumerate(utils.sliding_window(buffer, win_size=marker_size)):
        if len(set(window)) == marker_size:
            return i + marker_size


def main():
    input_txt = utils.get_input(6).strip()

    print(f"Part1: {part1(input_txt)}")
    print(f"Part2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
