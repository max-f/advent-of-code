#!/usr/bin/env python

import re

from utils import utils

"""
Code for https://adventofcode.com/2023/day/5
"""


def part1(seeds: list[int], mappings) -> int:
    final_numbers = []
    for n in seeds:
        for mapping in mappings:
            n = get_number(n, mapping)

        final_numbers.append(n)
    return min(final_numbers)


def part2(seeds, mappings) -> int:
    x = 1
    reversed_mappings = mappings[::-1]

    while True:
        seed = x
        for mapping in reversed_mappings:
            seed = get_number_inv(seed, mapping)

        if is_in_range(seed, seeds):
            return x
        x += 1


def create_mapping(lines):
    return [list(map(int, re.findall("-?\d+", x))) for x in lines]


def get_number(n, mapping):
    for range_spec in mapping:
        if range_spec[1] <= n < range_spec[1] + range_spec[2]:
            return range_spec[0] + (n - range_spec[1])
    return n


def get_number_inv(n, mapping):
    for range_spec in mapping:
        if range_spec[0] <= n < range_spec[0] + range_spec[2]:
            return range_spec[1] + (n - range_spec[0])
    return n


def is_in_range(n, seeds):
    return any(
        start <= n < start + amount for start, amount in zip(seeds[::2], seeds[1::2])
    )


def main():
    input_txt = utils.get_input(5)
    chunks = input_txt.strip().split("\n\n")

    chunks = [chunk.strip() for chunk in chunks]
    seeds = utils.ints(chunks[0])

    mappings = [create_mapping(chunk.split("\n")[1:]) for chunk in chunks[1:]]

    print(f"Part1: {part1(seeds, mappings)}")
    print(f"Part2: {part2(seeds, mappings)}")


if __name__ == "__main__":
    main()
