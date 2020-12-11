#!/usr/bin/env python

from utils import utils
from functools import lru_cache

"""
Code for https://adventofcode.com/2020/day/10
"""


def part1(numbers: list[int]) -> int:
    device_joltage = max(numbers) + 3
    sorted_adapters = sorted(numbers)

    sorted_adapters.insert(0, 0)
    sorted_adapters.append(device_joltage)

    diff_1 = 0
    diff_3 = 0
    for i in range(1, len(sorted_adapters)):
        current = sorted_adapters[i]
        previous = sorted_adapters[i - 1]

        if current - previous == 1:
            diff_1 += 1
        elif current - previous == 3:
            diff_3 += 1
    return diff_1 * diff_3


def edges(numbers: frozenset[int], start: int) -> list[int]:
    return [start + i for i in [1, 2, 3] if start + i in numbers]


@lru_cache
def search(numbers: frozenset[int], start: int, limit: int) -> int:
    if start == limit:
        return 1

    total = 0
    for e in edges(numbers, start):
        total += search(numbers, e, limit)
    return total


def part2(numbers: list[int]) -> int:
    device_joltage = max(numbers) + 3
    numbers.append(device_joltage)
    return search(frozenset(numbers), 0, device_joltage)


def main():
    input_txt = utils.get_input(10).rstrip()
    numbers = utils.ints(input_txt)
    print(part1(numbers))
    print(part2(numbers))


if __name__ == "__main__":
    main()
