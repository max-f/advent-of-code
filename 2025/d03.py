#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2025/day/3
"""


def select_n_numbers(bank: list[int], count: int) -> list[int]:
    max_numbers = []
    start_idx = 0
    n = len(bank)

    for pos in range(count):
        end_idx = n - (count - pos - 1)
        max_idx = max(range(start_idx, end_idx), key=lambda i: bank[i])
        max_numbers.append(bank[max_idx])
        start_idx = max_idx + 1

    return max_numbers


def part1(banks) -> int:
    total = 0
    for bank in banks:
        numbers = select_n_numbers(bank, 2)
        total += int("".join(map(str, numbers)))
    return total


def part2(banks) -> int:
    total = 0
    for bank in banks:
        numbers = select_n_numbers(bank, 12)
        total += int("".join(map(str, numbers)))
    return total


def parse_input(input_txt: str) -> list[list[int]]:
    return [[int(c) for c in line] for line in input_txt.strip().split("\n")]


def main():
    input_txt = utils.get_input(3)
    banks = parse_input(input_txt)
    print(f"Part1: {part1(banks)}")
    print(f"Part2: {part2(banks)}")


if __name__ == "__main__":
    main()
