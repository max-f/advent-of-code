#!/usr/bin/env python

import networkx as nx

from utils import utils

# clockwise directions
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def create_graph(lines):
    G = nx.DiGraph()

    start = end = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                continue

            pos = (i, j)
            if c == "S":
                start = (pos, DIRECTIONS[0])
            elif c == "E":
                end = pos

            for d in DIRECTIONS:
                G.add_node((pos, d))

    for pos, d in G.nodes():
        # moving fwd
        new_pos = utils.tuple_add(pos, d)
        if (new_pos, d) in G.nodes():
            G.add_edge((pos, d), (new_pos, d), weight=1)

        # turning left/right
        for new_d in get_turn_directions(d):
            G.add_edge((pos, d), (pos, new_d), weight=1000)

    # create virtual end with incoming edges from all directions
    for direction in DIRECTIONS:
        if (end, direction) in G.nodes():
            G.add_edge((end, direction), "end", weight=0)

    return G, start


def get_turn_directions(direction):
    idx = DIRECTIONS.index(direction)
    return [DIRECTIONS[(idx - 1) % 4], DIRECTIONS[(idx + 1) % 4]]  # left  # right


def part1(G, start) -> int:
    return nx.shortest_path_length(G, start, "end", weight="weight")


def part2(G, start) -> int:
    paths = nx.all_shortest_paths(G, start, "end", weight="weight")
    positions = {pos for path in paths for pos, _ in path[:-1]}
    return len(positions)


def main() -> None:
    input_txt = utils.get_input(16)
    G, start = create_graph(input_txt.strip().split("\n"))

    print(f"Part1: {part1(G, start)}")
    print(f"Part2: {part2(G, start)}")


if __name__ == "__main__":
    main()
