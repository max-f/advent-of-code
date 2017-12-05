#!/usr/bin/env python

from typing import Callable, List


def part_one(xs: List[int]) -> int:
    return max(xs) - min(xs)


def part_two(xs: List[int]) -> int:
    for i, x in enumerate(xs):
        for y in xs[i + 1:]:
            if x % y == 0:
                return x // y
            elif y % x == 0:
                return y // x


def calculate_line_sum(filepath: str, fun: Callable[[List[int]], int]) -> sum:
    sum = 0
    with open(filepath, 'rt') as file_input:
        lines = file_input.readlines()
        for line in lines:
            xs = [int(x) for x in line.split()]
            sum += fun(xs)
    return sum


def main():
    filepath = '/home/keks/git/advent-of-code/2017/input/input{:02d}'.format(2)
    print('Sum part 1: {}'.format(calculate_line_sum(filepath, part_one)))
    print('Sum part 2: {}'.format(calculate_line_sum(filepath, part_two)))


if __name__ == '__main__':
    main()
