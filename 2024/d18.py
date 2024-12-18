#!/usr/bin/env python

import networkx as nx

from utils import utils

# clockwise directions
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
GRID_SIZE = 70


def create_graph(lines):
    G = nx.Graph()

    corrupted = set()
    for line in lines[:1024]:
        x, y = utils.ints(line)
        corrupted.add((x, y))

    for x in range(GRID_SIZE + 1):
        for y in range(GRID_SIZE + 1):
            if (x, y) in corrupted:
                continue
            for direction in DIRECTIONS:
                new_pos = utils.tuple_add((x, y), direction)
                if new_pos in corrupted:
                    continue
                G.add_edge((x, y), new_pos)

    return G


def part1(G) -> int:
    return nx.shortest_path_length(G, (0, 0), (GRID_SIZE, GRID_SIZE))


def part2(lines) -> tuple[int, int]:
    G = nx.Graph()

    corrupted = []
    for line in lines:
        x, y = utils.ints(line)
        corrupted.append((x, y))

    for x in range(GRID_SIZE + 1):
        for y in range(GRID_SIZE + 1):
            for direction in DIRECTIONS:
                new_pos = utils.tuple_add((x, y), direction)
                G.add_edge((x, y), new_pos)

    for bad_pos in corrupted:
        G.remove_node(bad_pos)
        try:
            nx.shortest_path_length(G, (0, 0), (70, 70))
        except nx.NetworkXNoPath:
            return bad_pos


def main() -> None:
    input_txt = utils.get_input(18)
    lines = input_txt.strip().split("\n")
    G = create_graph(lines)

    print(f"Part1: {part1(G)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
