#!/usr/bin/env python

import statistics

from utils import utils

"""
Code for https://adventofcode.com/2021/day/10
"""


def part2(lines: list[str]) -> int:
    values = {")": 1, "]": 2, "}": 3, ">": 4}
    pairs = {"(": ")", "[": "]", "<": ">", "{": "}"}
    pairs_reversed = {v: k for k, v in pairs.items()}

    scores = []
    for line in lines:
        bad_line = False
        stack = []
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            elif not stack or stack.pop() != pairs_reversed[c]:
                bad_line = True
                break

        if not bad_line:
            completion_chars = [pairs[c] for c in stack[::-1]]
            score = 0
            for c in completion_chars:
                score *= 5
                score += values[c]
            scores.append(score)

    return statistics.median(scores)


def part1(lines: list[str]) -> int:
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pairs = {"(": ")", "[": "]", "<": ">", "{": "}"}
    pairs_reversed = {v: k for k, v in pairs.items()}
    fails = []

    for line in lines:
        stack = []
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            elif not stack or stack.pop() != pairs_reversed[c]:
                fails.append(c)
                break

    return sum([values[c] for c in fails])


def main():
    input_txt = utils.get_input(10)
    lines = input_txt.strip().split("\n")

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
