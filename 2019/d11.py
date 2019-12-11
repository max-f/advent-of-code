#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints
from utils.intcode import Machine, State


class Direction(Enum):
    UP = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, -1)


def tuple_add(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


turn = {
    (0, Direction.UP): Direction.LEFT,
    (1, Direction.UP): Direction.RIGHT,
    (0, Direction.LEFT): Direction.DOWN,
    (1, Direction.LEFT): Direction.UP,
    (0, Direction.RIGHT): Direction.UP,
    (1, Direction.RIGHT): Direction.DOWN,
    (0, Direction.DOWN): Direction.RIGHT,
    (1, Direction.DOWN): Direction.LEFT
}


def run_robot(intcode, starting_tile):
    board = defaultdict(int)

    machine = Machine(0, copy.copy(intcode), deque(), 0)
    machine.inputs.append(starting_tile)
    state = machine.state
    position = (0, 0)
    facing = Direction.UP

    while state != State.HALT:
        state, out = machine.run()

        if len(out) != 2:
            raise Exception(f"Output from intcode machine != 2: {len(out)}")
        if out[0] == 0:
            board[position] = 0
        elif out[0] == 1:
            board[position] = 1
        else:
            raise Exception(f"First output value does not indicate black or white: {out[0]}")

        if out[1] != 0 and out[1] != 1:
            raise Exception(f"Second output value does not indicate left or right: {out[1]}")

        facing = turn[(out[1], facing)]
        position = tuple_add(position, facing.value)

        if state == State.WAIT_FOR_INPUT:
            machine.out.clear()
            machine.inputs.append(board[position])
            continue

    return board


def main():
    input_txt = get_input(11)
    int_code_list = ints(input_txt)
    code = defaultdict(int, enumerate(int_code_list))
    board1 = run_robot(code, 0)
    board2 = run_robot(code, 1)

    print(f'Part 1: {len(board1)}')
    width_min = min(board2.keys(), key=lambda x: x[0])[0]
    width_max = max(board2.keys(), key=lambda x: x[0])[0]
    height_min = min(board2.keys(), key=lambda x: x[1])[1]
    height_max = max(board2.keys(), key=lambda x: x[1])[1]
    print(f'{width_min} - {width_max} - {height_min} - {height_max}')
    for y in range(height_min, height_max + 1):
        line = ''
        for x in range(width_min, width_max + 1):
            if board2[(x, y)]:
                line += '\u2588'
            else:
                line += ' '
        print(line)


if __name__ == "__main__":
    main()
