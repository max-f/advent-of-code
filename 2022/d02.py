#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/2
"""

scores = {'X': 1, 'Y': 2, 'Z': 3,
          'A': 1, 'B': 2, 'C': 3}


def part1(lines: list[str]) -> int:
    wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    score = 0
    for line in lines:
        opp, me = line.split()
        if wins[opp] == me:
            score += 6
        elif draws[opp] == me:
            score += 3
    return score


def part2(lines: list[str]) -> int:
    wins = {'A': 'B', 'B': 'C', 'C': 'A'}
    losses = {'A': 'C', 'B': 'A', 'C': 'B'}
    score = 0
    for line in lines:
        opp, do = line.split()
        if do == 'X':
            score += scores[losses[opp]]
        elif do == 'Y':
            score += 3 + scores[opp]
        else:
            score += 6 + scores[wins[opp]]
    return score


def main():
    input_txt = utils.get_input(2)
    lines = [line for line in input_txt.split("\n") if line.strip()]

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
