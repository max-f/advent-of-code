#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/1
"""


def part1(calories: list[int]) -> int:
    return max(calories)


def part2(calories: list[int]) -> int:
    return sum(sorted(calories, reverse=True)[:3])


def main():
    input_txt = utils.get_input(1)
    calories = []
    counter = 0
    for line in input_txt.split("\n"):
        if line.strip():
            counter += int(line)
        else:
            calories.append(counter)
            counter = 0

    print(f"Part1: {part1(calories)}")
    print(f"Part2: {part2(calories)}")


if __name__ == "__main__":
    main()
