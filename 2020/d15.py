#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/15
"""


def part1(starting_numbers: list[int]) -> int:
    return calc_number(starting_numbers, 2020)


def part2(starting_numbers: list[int]) -> int:
    return calc_number(starting_numbers, 30000000)


def calc_number(starting_numbers: list[int], stop: int) -> int:
    mem = {}
    previous = None
    for i in range(stop):
        if i < len(starting_numbers):
            number = starting_numbers[i]
        elif previous in mem:
            number = i - 1 - mem[previous]
        else:
            number = 0
        mem[previous] = i - 1
        previous = number
    return previous


def main():
    input_txt = utils.get_input(15).rstrip()
    numbers = utils.ints(input_txt)
    print(part1(numbers))
    print(part2(numbers))


if __name__ == "__main__":
    main()
