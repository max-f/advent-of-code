#!/usr/bin/env python

import re
from utils import utils

"""
Code for https://adventofcode.com/2020/day/2
"""


def part1(all_text: str) -> int:
    total_valid = 0
    pattern = "(\d+)-(\d+) (\w): (\w+)"
    regex = re.compile(pattern)
    for line in all_text.split("\n"):
        match = regex.match(line)
        if not match:
            print("Hmm?")
            continue
        minimum = int(match.group(1))
        maximum = int(match.group(2))
        char = match.group(3)
        string = match.group(4)
        if minimum <= string.count(char) <= maximum:
            total_valid += 1
    return total_valid


def part2(all_text: str) -> int:
    total_valid = 0
    pattern = r"(\d+)-(\d+) (\w): (\w+)"
    regex = re.compile(pattern)
    for line in all_text.split("\n"):
        match = regex.match(line)
        if not match:
            print("Hmm?")
            continue
        pos1 = int(match.group(1))
        pos2 = int(match.group(2))
        char = match.group(3)
        string = match.group(4)
        if (list(string)[pos1 - 1] == char) ^ (list(string)[pos2 - 1] == char):
            total_valid += 1
    return total_valid


def main():
    input_txt = utils.get_input(2)
    print(part1(input_txt))
    print(part2(input_txt))


if __name__ == "__main__":
    main()
