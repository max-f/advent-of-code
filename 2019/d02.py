#!/usr/bin/env python

from utils import utils
import operator

opcode = {1: operator.add, 2: operator.mul, 99: None}


def process_opcode(starting_pos: int, value_list):
    operation = value_list[starting_pos]
    if not opcode[operation]:
        return False
    x = value_list[value_list[starting_pos + 1]]
    y = value_list[value_list[starting_pos + 2]]
    destination = value_list[starting_pos + 3]
    new_value = opcode[operation](x, y)
    value_list[destination] = new_value
    return True


def part1(input_txt: str) -> int:
    values = input_txt.split(',')
    value_list = [int(x) for x in values]
    value_list[1] = 12
    value_list[2] = 2
    starting_pos = 0
    while process_opcode(starting_pos, value_list):
        starting_pos += 4
    return value_list[0]


def part2(input_txt: str) -> int:
    target = 19690720

    values = input_txt.split(',')
    orig_value_list = [int(x) for x in values]

    for noun in range(100):
        for verb in range(100):
            starting_pos = 0
            value_list = list(orig_value_list)
            value_list[1] = noun
            value_list[2] = verb
            while process_opcode(starting_pos, value_list):
                starting_pos += 4
            if value_list[0] == target:
                return 100 * noun + verb


def main():
    input_txt = utils.get_input(2)
    p1 = part1(input_txt)
    p2 = part2(input_txt)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
