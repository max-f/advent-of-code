#!/usr/bin/env python

import networkx as nx

from utils import utils

"""
Code for https://adventofcode.com/2021/day/12
"""


def part1(G, node):
    if node == "end":
        return 1

    G.nodes[node]["seen"] += 1
    paths = 0

    for n in nx.neighbors(G, node):
        if G.nodes[n]["seen"] == 0 or n.isupper():
            paths += part1(G, n)

    G.nodes[node]["seen"] -= 1
    return paths


def part2(G, node, seen_twice):
    if node == "end":
        return 1

    G.nodes[node]["seen"] += 1
    paths = 0

    for n in nx.neighbors(G, node):
        if G.nodes[n]["seen"] == 0 or n.isupper():
            paths += part2(G, n, seen_twice)
        elif not seen_twice and G.nodes[n]["seen"] == 1 and n != "start":
            paths += part2(G, n, True)

    G.nodes[node]["seen"] -= 1
    return paths


def main():
    input_txt = utils.get_input(12)
    G = nx.Graph()
    for line in input_txt.splitlines():
        source, dest = line.split("-")
        G.add_edge(source, dest)

    for node in G:
        G.nodes[node]["seen"] = 0

    start = "start"
    print(f"Part 1: {part1(G, start)}")
    print(f"Part 2: {part2(G, start, False)}")


if __name__ == "__main__":
    main()
