#!/usr/bin/env python

import re
from utils import utils

"""
Code for https://adventofcode.com/2020/day/6
"""


def part1(all_groups: list[str]) -> int:
    total = 0
    for group in all_groups:
        persons = group.split("\n")
        group_answers = set()
        for person in persons:
            group_answers.update(person)
        total += len(group_answers)
    return total


def part2(all_groups: list[str]) -> int:
    total = 0
    for group in all_groups:
        common = calculate_common_answers(group)
        total += common
    return total


def calculate_common_answers(group: str) -> int:
    persons = group.split("\n")
    group_answers = set()
    for person in persons:
        if group_answers:
            group_answers = group_answers & set(person)
            if not group_answers:
                return 0
        else:
            group_answers.update(set(person))
    return len(group_answers)


def main():
    input_txt = utils.get_input(6).rstrip()
    all_groups = re.split(r"\n\s*\n", input_txt)
    print(part1(all_groups))
    print(part2(all_groups))


if __name__ == "__main__":
    main()
