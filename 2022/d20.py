#!/usr/bin/env python

from utils import utils
from typing import List

"""
Code for https://adventofcode.com/2022/day/20
"""


class Node:
    def __init__(self, value, prv=None, nxt=None):
        self.value = value
        self.prv = prv
        self.nxt = nxt


def part1(input_txt: str):
    numbers = [Node(int(line)) for line in input_txt.split("\n")]
    link_numbers(numbers)

    mix_numbers(numbers)

    return find_groove_coordinates(numbers)


def part2(input_txt: str):
    numbers = [Node(int(line) * 811589153) for line in input_txt.split("\n")]
    link_numbers(numbers)

    for _ in range(10):
        mix_numbers(numbers)

    return find_groove_coordinates(numbers)


def link_numbers(numbers: List[Node]) -> None:
    for a, b in zip(numbers, numbers[1:]):
        a.nxt = b
        b.prv = a

    numbers[-1].nxt = numbers[0]
    numbers[0].prv = numbers[-1]


def mix_numbers(numbers: List[Node]) -> None:
    for x in numbers:
        x.prv.nxt = x.nxt
        x.nxt.prv = x.prv
        a, b = x.prv, x.nxt
        moves = x.value % (len(numbers) - 1)
        for _ in range(moves):
            a = a.nxt
            b = b.nxt
        a.nxt = x
        x.prv = a
        b.prv = x
        x.nxt = b


def find_groove_coordinates(numbers: List[Node]) -> int:
    result = 0
    for x in numbers:
        if x.value == 0:
            tmp = x
            for _ in range(3):
                for _ in range(1000):
                    tmp = tmp.nxt
                result += tmp.value
    return result


def main():
    input_txt = utils.get_input(20).strip()

    print(f"Part 1: {part1(input_txt)}")
    print(f"Part 2: {part2(input_txt)}")


if __name__ == "__main__":
    main()
