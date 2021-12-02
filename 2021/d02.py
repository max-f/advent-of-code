#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2021/day/2
"""


def part1(lines: list[str]) -> int:
    horizontal_pos = depth = 0
    for line in lines:
        instr, number = line.split()
        if instr == "forward":
            horizontal_pos += int(number)
        elif instr == "up":
            depth -= int(number)
        else:
            depth += int(number)
    return horizontal_pos * depth


def part2(lines: list[str]) -> int:
    horizontal_pos = depth = aim = 0

    def forward(value: int) -> None:
        nonlocal horizontal_pos, depth, aim
        horizontal_pos += value
        depth += aim * value

    def up(value: int) -> None:
        nonlocal aim
        aim -= value

    def down(value: int) -> None:
        nonlocal aim
        aim += value

    instructions = {"forward": forward, "up": up, "down": down}
    for line in lines:
        instr, number = line.split()
        instructions[instr](int(number))

    return horizontal_pos * depth


def main():
    input_txt = utils.get_input(2)
    instructions = input_txt.strip().split("\n")
    print(part1(instructions))
    print(part2(instructions))


if __name__ == "__main__":
    main()
