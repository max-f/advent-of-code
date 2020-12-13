#!/usr/bin/env python

from utils import utils
import math

"""
Code for https://adventofcode.com/2020/day/13
"""


def part1(depart_time: int, buses: list[int]) -> int:
    wait, bus_id = min((bus - depart_time % bus, bus) for bus in buses if bus)
    return wait * bus_id


def part2(buses: list[int]) -> int:
    """
    Only by looking at hints from AoC reddit:
    Compare https://brilliant.org/wiki/chinese-remainder-theorem/
    """
    x = 0
    N = math.prod(bus for bus in buses if bus)
    for i, bus in enumerate(buses):
        if not bus:
            continue
        y_i = N // bus
        # See https://docs.python.org/3/library/functions.html#pow
        z_i = pow(y_i, -1, bus)
        x += (-i) * y_i * z_i
    return x % N


def main():
    input_txt = utils.get_input(13).rstrip()
    line_1, line_2 = input_txt.split("\n")
    depart_time = int(line_1)
    buses = [int(b) if b != "x" else None for b in line_2.split(",")]

    print(part1(depart_time, buses))
    print(part2(buses))


if __name__ == "__main__":
    main()
