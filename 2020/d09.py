#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/9
"""


def find_2sum(numbers: list[int], searched: int) -> tuple:
    seen = set()
    for x in numbers:
        y = searched - x
        if y in seen:
            return x, y
        else:
            seen.add(x)
    return ()


def part1(numbers: list[int], window_size: int = 25):
    if window_size >= len(numbers):
        return None
    for i in range(window_size, len(numbers)):
        searched = numbers[i]
        pre_window = numbers[i - window_size : i]
        if not find_2sum(pre_window, searched):
            return searched


def part2(numbers: list[int], non_valid: int) -> int:
    for s in range(len(numbers) // 4, 2, -1):
        for window in utils.sliding_window(numbers, s):
            if sum(window) == non_valid:
                return min(window) + max(window)


def main():
    input_txt = utils.get_input(9).rstrip()
    numbers = utils.ints(input_txt)
    non_valid = part1(numbers)
    print(non_valid)
    print(part2(numbers, non_valid))


if __name__ == "__main__":
    main()
