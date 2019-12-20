#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints, tuple_add
from utils.intcode import Machine
import bisect
import networkx as nx
from pprint import pprint


def create_board(input_txt):
    board = defaultdict(str)
    m = [line for line in input_txt.split('\n')]
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            board[(x, y)] = c
    return board


def part1() -> int:
    pass


def part2() -> int:
    pass


def main():
    input_txt = get_input(83)

    board = create_board(input_txt)
    width = max(x for x, y in board.keys())
    height = max(y for x, y in board.keys())

    # for x in range(width):
    # G = nx.Graph()


if __name__ == "__main__":
    main()
