#!/usr/bin/env python

import networkx as nx

from utils import utils

"""
Code for https://adventofcode.com/2022/day/12
"""


def part1(G, start, end) -> int:
    return nx.shortest_path_length(G, start, end)


def part2(G, grid, end) -> int:
    starting_points = [t for t, v in grid.items() if v == "a"]

    shortest = 999
    for s in starting_points:
        try:
            possible_path_length = nx.shortest_path_length(G, s, end)
        except nx.exception.NetworkXNoPath:
            continue
        if possible_path_length < shortest:
            shortest = possible_path_length
    return shortest


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

    G = nx.DiGraph()
    for coord, v in grid.items():
        neighbors = [utils.tuple_add(coord, a) for a in adjacent]
        neighbors = [t for t in neighbors if t in grid]
        for n in neighbors:
            if -(ord(v) - ord(grid[n])) <= 1:
                G.add_edge(coord, n)

    print(f"Part1: {part1(G, start, end)}")
    print(f"Part2: {part2(G, grid, end)}")


if __name__ == "__main__":
    main()
