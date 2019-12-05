#!/usr/bin/env python

import operator
from typing import List

from utils import utils

POINTER = 0
INPUT = 0


def op_input(idx: int, intcode: List[int]):
    intcode[idx] = INPUT


def op_output(idx: int, intcode: List[int]):
    print(f'OUTPUT: {intcode[idx]}')


def op_jump_true(x: int, idx: int):
    global POINTER
    if x != 0:
        POINTER = idx
    else:
        POINTER += 3


def op_jump_false(x: int, idx: int):
    global POINTER
    if x == 0:
        POINTER = idx
    else:
        POINTER += 3


def op_lt(x: int, y: int) -> int:
    if x < y:
        return 1
    return 0


def op_eq(x: int, y: int) -> int:
    if x == y:
        return 1
    return 0


operation = {
    1: (operator.add, 4),
    2: (operator.mul, 4),
    3: (op_input, 2),
    4: (op_output, 2),
    5: (op_jump_true, 0),
    6: (op_jump_false, 0),
    7: (op_lt, 4),
    8: (op_eq, 4),
    99: (None, None)
}


def process_opcode(intcode: List[int]):
    global POINTER

    modes_and_opcode = [int(x) for x in str(intcode[POINTER]).zfill(5)]
    p1_mode = modes_and_opcode[2]
    p2_mode = modes_and_opcode[1]
    p3_mode = modes_and_opcode[0]
    opcode = int("".join(map(str, modes_and_opcode[-2:])))

    op, op_length = operation[opcode]
    if not op:
        return False

    # Handle in and out
    if op_length == 2:
        if p1_mode:
            op(POINTER + 1, intcode)
        else:
            op(intcode[POINTER + 1], intcode)

    # Handle add, mul, lt, eq
    if op_length == 4:
        if p1_mode:
            x = intcode[POINTER + 1]
        else:
            x = intcode[intcode[POINTER + 1]]
        if p2_mode:
            y = intcode[POINTER + 2]
        else:
            y = intcode[intcode[POINTER + 2]]
        if p3_mode:
            destination = POINTER + 3
        else:
            destination = intcode[POINTER + 3]
        new_value = op(x, y)
        intcode[destination] = new_value

    # Handle jumps
    if op_length == 0:
        if p1_mode:
            x = intcode[POINTER + 1]
        else:
            x = intcode[intcode[POINTER + 1]]
        if p2_mode:
            idx = intcode[POINTER + 2]
        else:
            idx = intcode[intcode[POINTER + 2]]
        op(x, idx)
    POINTER += op_length
    return True


def calculate(intcode: List[int]) -> None:
    while process_opcode(intcode):
        print(f'POINTER: {POINTER}')
        continue


def main():
    global INPUT
    INPUT = 5
    input_txt = utils.get_input(5)
    intcode = utils.ints(input_txt)
    calculate(intcode)


if __name__ == "__main__":
    main()
