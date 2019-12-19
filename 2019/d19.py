#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from utils.intcode import Machine
from utils.utils import get_input, ints


def part1(intcode) -> int:
    total_affected = 0
    for y in range(50):
        for x in range(50):
            pos_in = position_in_beam(intcode, x, y)
            total_affected += pos_in
    return total_affected


def part2(intcode, n=100) -> int:
    x = 100
    y = 100
    while not position_in_beam(intcode, x + (n - 1), y):
        y += 1
        while not position_in_beam(intcode, x, y + (n - 1)):
            x += 1
    return x * 10000 + y


def position_in_beam(intcode, x, y):
    machine = Machine(0, copy.copy(intcode), deque(), 0)
    machine.inputs.append(x)
    machine.inputs.append(y)
    return bool(machine.run()[-1][0])


def main():
    input_txt = get_input(19)
    int_code_list = ints(input_txt)
    code = defaultdict(int, enumerate(int_code_list))
    p1 = part1(code)
    print(f"Part 1: {p1}")

    p2 = part2(code)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
