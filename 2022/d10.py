#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/10
"""


def part1(register: list[int]) -> int:
    signal_strength = 0
    for cycle in range(20, 221, 40):
        strength = cycle * register[cycle - 1]
        signal_strength += strength
    return signal_strength


def part2(register: list[int]) -> None:
    for i, x in enumerate(register):
        print("█" if abs(i % 40 - x) <= 1 else " ", end="" if (i + 1) % 40 else "\n")


def main():
    input_txt = utils.get_input(10).strip()

    register = [1]

    for line in input_txt.split("\n"):
        cmd, *args = line.strip().split()
        if cmd == "noop":
            register.append(register[-1])
        else:
            value = int(args[0])
            register.append(register[-1])
            register.append(register[-1] + value)

    print(f"Part1: {part1(register)}")
    print(f"Part2:")
    part2(register)


if __name__ == "__main__":
    main()
