#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/3
"""


def part1(lines: list[str]) -> int:
    score = 0
    for line in lines:
        complete = list(line)
        first_comp = set(complete[: len(complete) // 2])
        second_comp = set(complete[len(complete) // 2 :])
        (common,) = first_comp.intersection(second_comp)
        score += prio(common)
    return score


def part2(lines: list[str]) -> int:
    score = 0
    for i in range(0, len(lines), 3):
        group = lines[i : i + 3]
        (first, second, third) = group
        (common,) = set(first).intersection(set(second)).intersection(set(third))
        score += prio(common)
    return score


def prio(ch: str) -> int:
    if ch.islower():
        return ord(ch) - ord("a") + 1
    else:
        return ord(ch) - ord("A") + 26 + 1


def main():
    input_txt = utils.get_input(3)
    lines = [line for line in input_txt.split("\n") if line.strip()]

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
