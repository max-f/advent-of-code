#!/usr/bin/env python

from utils import utils
import networkx as nx
from pprint import pprint

"""
Code for https://adventofcode.com/2022/day/12
"""


def part1() -> int:
    pass


def part2() -> None:
    pass


adjacent = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]


def main():
    input_txt = utils.get_input(12).strip()
    grid = {}
    start = None
    end = None

    for y, line in enumerate(input_txt.strip().split("\n")):
        for x, value in enumerate(line):
            if value == "S":
                start = (x, y)
                grid[x, y] = "a"
            elif value == "E":
                end = (x, y)
                grid[x, y] = "z"
            else:
                grid[x, y] = value

    # pprint(grid)
    G = nx.DiGraph()
    for coord, v in grid.items():
        neighbors = [utils.tuple_add(coord, a) for a in adjacent]
        neighbors = [t for t in neighbors if t in grid]
        for n in neighbors:
            if -(ord(v) - ord(grid[n])) <= 1:
                G.add_edge(coord, n)
    l = nx.shortest_path_length(G, start, end)
    # print(G.edges)
    print(f"Part 1: {l}")

    starting_points = [t for t, v in grid.items() if v == "a"]
    print(starting_points)

    shortest = 999
    for s in starting_points:
        try:
            l = nx.shortest_path_length(G, s, end)
        except:
            continue
        if l < shortest:
            shortest = l
    print(shortest)

    # print(f"Part1: {part1()}")
    # print(f"Part2:")


if __name__ == "__main__":
    main()
