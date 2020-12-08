#!/usr/bin/env python

from utils import utils
import copy

"""
Code for https://adventofcode.com/2020/day/8
"""


def part1(operations: dict[int, tuple[str, int]]) -> int:
    return run(operations)[1]


def part2(operations: dict[int, tuple[str, int]]) -> int:
    candidates = [k for k, v in operations.items() if v[0] in ["jmp", "nop"]]

    is_loop, accumulator = run(operations)
    while is_loop and candidates:
        new_operations = copy.deepcopy(operations)
        change = candidates.pop()
        operation = new_operations[change]
        if operation[0] == "jmp":
            new_operations[change] = ("nop", operation[1])
        else:
            new_operations[change] = ("jmp", operation[1])

        is_loop, accumulator = run(new_operations)
    return accumulator


def run(operations: dict[int, tuple[str, int]]) -> tuple[bool, int]:
    accumulator = 0
    pointer = 0
    done = set()

    while pointer not in done:
        if pointer == max(operations) + 1:
            return False, accumulator
        done.add(pointer)
        next_op, number = operations[pointer]
        if next_op == "jmp":
            pointer += number
            continue
        elif next_op == "acc":
            accumulator += number
        pointer += 1

    return True, accumulator


def main():
    input_txt = utils.get_input(8).rstrip()
    operations = {}
    for idx, line in enumerate(input_txt.split("\n")):
        operation, number = line.split()
        operations[idx] = (operation, int(number))

    print(part1(operations))
    print(part2(operations))


if __name__ == "__main__":
    main()
