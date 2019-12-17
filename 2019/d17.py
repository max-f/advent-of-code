#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints, tuple_add
from utils.intcode import Machine, State


class Direction(Enum):
    UP = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, -1)


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


def run_robot(intcode):
    board = defaultdict(int)

    machine = Machine(0, copy.copy(intcode), deque(), 0)
    # machine.inputs.append(starting_tile)
    state = machine.state
    position = (0, 0)
    view = ''

    while state != State.HALT:
        state, out = machine.run()

        view += ''.join(list(map(chr, out)))

    print(view)
    return board


def main():
    input_txt = get_input(17)
    int_code_list = ints(input_txt)
    code = defaultdict(int, enumerate(int_code_list))
    board1 = run_robot(code)

    print(f'Part 1: {len(board1)}')


if __name__ == "__main__":
    main()
