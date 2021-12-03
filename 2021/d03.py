#!/usr/bin/env python

import copy

from utils import utils

"""
Code for https://adventofcode.com/2021/day/3
"""


def find_least_and_most_common_bits(
    bit_lines: list[str],
) -> tuple[list[str], list[str]]:
    bit_positions = [0] * len(bit_lines[0])
    total = len(bit_lines)
    for bits in bit_lines:
        for i, bit in enumerate(bits):
            if bit == "1":
                bit_positions[i] += 1
    most_common_bits = ["1" if x >= (total / 2) else "0" for x in bit_positions]
    least_common_bits = ["1" if x < (total / 2) else "0" for x in bit_positions]
    return least_common_bits, most_common_bits


def part1(bit_lines: list[str]) -> int:
    least_common_bits, most_common_bits = find_least_and_most_common_bits(bit_lines)
    return int("".join(most_common_bits), 2) * int("".join(least_common_bits), 2)


def part2(bit_lines: list[str]) -> int:
    length = len(bit_lines[0])
    oxy_lines = copy.deepcopy(bit_lines)
    co2_lines = copy.deepcopy(bit_lines)

    for i in range(length):
        least_common, most_common = find_least_and_most_common_bits(oxy_lines)
        filter_number = most_common[i]
        oxy_lines = [bit_line for bit_line in oxy_lines if bit_line[i] == filter_number]
        if len(oxy_lines) == 1:
            break

    for i in range(length):
        least_common, most_common = find_least_and_most_common_bits(co2_lines)
        filter_number = least_common[i]
        co2_lines = [bit_line for bit_line in co2_lines if bit_line[i] == filter_number]
        if len(co2_lines) == 1:
            break

    return int("".join(oxy_lines[0]), 2) * int("".join(co2_lines[0]), 2)


def main():
    input_txt = utils.get_input(3)
    bit_lines = input_txt.strip().split("\n")

    print(f"Part 1: {part1(bit_lines)}")
    print(f"Part 2: {part2(bit_lines)}")


if __name__ == "__main__":
    main()
