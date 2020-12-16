#!/usr/bin/env python

import math
from collections import defaultdict
from utils import utils

"""
Code for https://adventofcode.com/2020/day/16
"""


def part1(valid_ranges: dict[str, set[int]], nearby: str) -> tuple[int, list[str]]:
    not_valid = []
    valid_nearby = []

    valid_numbers = set().union(*valid_ranges.values())
    for line in nearby.split("\n"):
        all_numbers = utils.ints(line)
        is_valid = True
        for n in all_numbers:
            if n not in valid_numbers:
                not_valid.append(n)
                is_valid = False
        if all_numbers and is_valid:
            valid_nearby.append(line)

    return sum(not_valid), valid_nearby


def part2(
    my_ticket: str, ranges: dict[str, set[int]], valid_nearby_lines: list[str]
) -> int:
    positions = get_numbers_for_index(valid_nearby_lines)
    classification = create_index_to_name_classification(ranges, positions)

    assign_index_to_unique_name(classification)
    indices = [
        i
        for i, names in classification.items()
        if names and names[0].startswith("departure")
    ]
    return math.prod([utils.ints(my_ticket)[i] for i in indices])


def create_index_to_name_classification(
    ranges: dict[str, set[int]], positions: dict[int, set[int]]
) -> dict[int, list[str]]:
    classification = {}
    for i, nums in positions.items():
        for name, valid in ranges.items():
            is_valid = [True if x in valid else False for x in nums]
            if all(is_valid):
                if i in classification:
                    classification[i].append(name)
                else:
                    classification[i] = [name]
    return classification


def get_numbers_for_index(valid_nearby_lines: list[str]) -> dict[int, set[int]]:
    positions = defaultdict(set)
    for n in valid_nearby_lines:
        all_numbers = utils.ints(n)
        for i, x in enumerate(all_numbers):
            positions[i].add(x)
    return positions


def assign_index_to_unique_name(classification: dict[int, list[str]]) -> None:
    """
    Using  side effects on classification dict :E
    """
    while not len(get_valid_classifications(classification)) == len(classification):
        valid_classifications = get_valid_classifications(classification)
        for i, name in valid_classifications:
            for j, names in classification.items():
                if i == j:
                    continue
                if name in names:
                    classification[j].remove(name)


def get_valid_classifications(
    classification: dict[int, list[str]]
) -> list[tuple[int, str]]:
    return [(i, names[0]) for i, names in classification.items() if len(names) == 1]


def read_ranges(ranges: str) -> dict[str, set[int]]:
    valid = {}
    for line in ranges.split("\n"):
        name = line.split(":")[0]
        valid_range = set()
        a, b, c, d = map(abs, utils.ints(line))
        valid_range.update(set(range(a, b + 1)))
        valid_range.update(set(range(c, d + 1)))
        valid[name] = valid_range
    return valid


def main():
    input_txt = utils.get_input(16).rstrip()
    ranges, my_ticket, nearby = input_txt.split("\n\n")

    valid_ranges = read_ranges(ranges)
    sum_not_valid, valid_nearby_lines = part1(valid_ranges, nearby)
    print(sum_not_valid)
    print(part2(my_ticket, valid_ranges, valid_nearby_lines))


if __name__ == "__main__":
    main()
