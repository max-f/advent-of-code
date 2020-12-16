#!/usr/bin/env python

from utils import utils
from pprint import pprint
from collections import defaultdict
import math

"""
Code for https://adventofcode.com/2020/day/16
"""


def part1(valid: set[int], nearby: str) -> tuple[int, list[str]]:
    not_valid = []
    valid_nearby = []
    for line in nearby.split('\n'):
        all_numbers = utils.ints(line)
        is_valid = True
        for n in all_numbers:
            if n not in valid:
                not_valid.append(n)
                is_valid = False
        if all_numbers and is_valid:
            valid_nearby.append(line)

    return sum(not_valid), valid_nearby


def part2(my_ticket: str, ranges: dict[str, set[int]], valid_nearby: list[str]) -> int:
    classification = dict()

    positions = defaultdict(set)
    for n in valid_nearby:
        all_numbers = utils.ints(n)
        for i, x in enumerate(all_numbers):
            positions[i].add(x)


    for i, nums in positions.items():
        for name, valid in ranges.items():
            is_valid = [True if x in valid else False for x in nums]
            if all(is_valid):
                if i in classification:
                    classification[i].append(name)
                else:
                    classification[i] = [name]

    while not len(get_valid_classifications(classification)) == len(classification):
        valid_classifications = get_valid_classifications(classification)
        for i, name in valid_classifications:
            for j, names in classification.items():
                if i == j:
                    continue
                if name in names:
                    classification[j].remove(name)

    indices = [i for i, names in classification.items() if names and names[0].startswith('departure')]
    my_numbers = utils.ints(my_ticket)
    product = 1
    for i in indices:
        product *= my_numbers[i]
    return product


def get_valid_classifications(classification):
    valid = []
    for i, names in classification.items():
        if len(names) == 1:
            valid.append((i, names[0]))
    return valid


def valid_class(classification: dict[int, list[str]]):
    unique = [True if len(v) == 1 else False for i, v in classification]
    return all(unique)


def get_valid_ranges(ranges: str):
    valid = set()
    for line in ranges.split('\n'):
        a, b, c, d = map(abs, utils.ints(line))
        valid.update(set(range(a, b + 1)))
        valid.update(set(range(c, d + 1)))
    return valid


def get_ranges(ranges: str):
    valid = {}
    for line in ranges.split('\n'):
        name = line.split(':')[0]
        valid_range = set()
        a, b, c, d = map(abs, utils.ints(line))
        valid_range.update(set(range(a, b + 1)))
        valid_range.update(set(range(c, d + 1)))
        valid[name] = valid_range
    return valid


def main():
    input_txt = utils.get_input(16).rstrip()
    ranges, my_ticket, nearby = input_txt.split('\n\n')
    valid = get_valid_ranges(ranges)

    p1, valid_nearby = part1(valid, nearby)
    print(p1)

    valid_ranges = get_ranges(ranges)
    print(part2(my_ticket, valid_ranges, valid_nearby))


if __name__ == "__main__":
    main()
