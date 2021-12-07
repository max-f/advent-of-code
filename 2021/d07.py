#!/usr/bin/env python

import statistics

from utils import utils

"""
Code for https://adventofcode.com/2021/day/7
"""


def part1(positions: list[int]) -> int:
    median = statistics.median(positions)
    return sum([abs(pos - median) for pos in positions])


def fuel_price_p2(moves: int) -> int:
    return (moves + 1) * moves // 2


def part2(positions: list[int]) -> int:
    minimum = float("inf")
    for x in range(min(positions), max(positions) + 1):
        current = sum([fuel_price_p2(abs(x - pos)) for pos in positions])
        if current < minimum:
            minimum = current
    return minimum


def main():
    input_txt = utils.get_input(7)
    positions = utils.ints(input_txt)
    print(f"Part 1: {part1(positions)}")
    print(f"Part 2: {part2(positions)}")


if __name__ == "__main__":
    main()
