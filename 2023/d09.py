#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2023/day/9
"""


def predict(series: list[int], p2: bool) -> int:
    diffs = [series]
    while not all(x == 0 for x in diffs[-1]):
        diffs.append([b - a for a, b in zip(diffs[-1], diffs[-1][1:])])
    last = 0
    for series in reversed(diffs[:-1]):
        last = series[0] - last if p2 else series[-1] + last
    return last


def part1(line_series: list[list[int]]) -> int:
    return sum(predict(line, False) for line in line_series)


def part2(line_series: list[list[int]]) -> int:
    return sum(predict(line, True) for line in line_series)


def main():
    input_txt = utils.get_input(9)
    line_series = [utils.ints(line) for line in input_txt.strip().split("\n")]

    print(f"Part1: {part1(line_series)}")
    print(f"Part2: {part2(line_series)}")


if __name__ == "__main__":
    main()
