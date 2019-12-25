#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints, tuple_add
from utils.intcode import Machine
import bisect
import networkx as nx
from pprint import pprint

start = ()
end = ()


def create_board(input_txt):
    board = defaultdict(str)
    m = [line for line in input_txt.split('\n')]
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            board[(x, y)] = c
    return board


def add_portal(G, portals, portal, pos):
    global start, end

    if portal == 'AA':
        start = pos
    elif portal == 'ZZ':
        end = pos
    elif portal in portals:
        G.add_edge(pos, portals[portal], portal=True)
    else:
        portals[portal] = pos


def part1() -> int:
    pass


def part2() -> int:
    pass


def main():
    input_txt = get_input(83)

    G = nx.Graph()
    portals = {}

    board = create_board(input_txt)
    width = max(x for x, y in board.keys())
    height = max(y for x, y in board.keys())

    for x in range(width):
        for y in range(height):
            c_at_pos = board[(x, y)]
            if c_at_pos != '.':
                continue

            right = board[(x + 1, y)]
            if right == '.':
                G.add_edge((x, y), (x + 1, y))
            elif right.isupper():
                portal = right + board[(x + 2, y)]
                if portal.isupper():
                    add_portal(G, portals, portal, (x, y))

            down = board[(x, y + 1)]
            if down == '.':
                G.add_edge((x, y), (x, y + 1))
            elif down.isupper():
                portal = down + board[(x, y + 2)]
                if portal.isupper():
                    add_portal(G, portals, portal, (x, y))

            up = board[(x, y - 1)]
            if up.isupper():
                portal = up + board[(x, y - 2)]
                if portal.isupper():
                    add_portal(G, portals, portal, (x, y))

            left = board[(x - 1, y)]
            if left.isupper():
                portal = left + board[(x - 2, y)]
                if portal.isupper():
                    add_portal(G, portals, portal, (x, y))

    print(G.edges.data())
    print(f'Start pos: {start}')
    print(f'End pos: {end}')
    shortest_path = nx.shortest_path(G, start, end)
    result = nx.shortest_path_length(G, start, end)
    pprint(shortest_path)
    print(f'Part 1: {result}')


if __name__ == "__main__":
    main()
