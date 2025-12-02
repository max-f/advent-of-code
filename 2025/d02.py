#!/usr/bin/env python
from utils import utils

"""
Code for https://adventofcode.com/2025/day/2
"""


def part1(sections: list[tuple[int, int]]) -> int:
    sum_invalids = 0
    for start, end in sections:
        for i in range(start, end + 1):
            s = str(i)
            if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]:
                sum_invalids += i
    return sum_invalids


def is_invalid(s: str) -> bool:
    for j in range(len(s) // 2, 0, -1):
        if len(s) % j != 0:
            continue
        split_str = [s[i:i + j] for i in range(0, len(s), j)]
        if len(set(split_str)) == 1:
            return True
    return False


def part2(sections: list[tuple[int, int]]) -> int:
    sum_invalids = 0
    for start, end in sections:
        for i in range(start, end + 1):
            s = str(i)
            if is_invalid(s):
                sum_invalids += i
    return sum_invalids


def parse_input(input_txt: str) -> list[tuple[int, ...]]:
    return [
        tuple(map(int, section.split("-")))
        for section in input_txt.strip().split(",")
    ]


def main():
    input_txt = utils.get_input(2)
    sections = parse_input(input_txt)
    print(f"Part1: {part1(sections)}")
    print(f"Part2: {part2(sections)}")


if __name__ == "__main__":
    main()
