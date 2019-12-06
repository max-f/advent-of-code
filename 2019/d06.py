#!/usr/bin/env python

from utils import utils
import networkx as nx


def part1(input_txt) -> int:
    G = nx.DiGraph()
    for line in input_txt.rstrip().split('\n'):
        print(line)
        node1, node2 = line.split(')')
        G.add_edge(node1, node2)
    total = 0
    for node in list(G.nodes()):
        total += len(nx.ancestors(G, node))
    return total


def part2(input_txt, x, y) -> int:
    G = nx.DiGraph()
    for line in input_txt.rstrip().split('\n'):
        print(line)
        node1, node2 = line.split(')')
        G.add_edge(node1, node2)
    orbit_a = list(G.predecessors(x))[0]
    orbit_b = list(G.predecessors(y))[0]
    undirected_graph = G.to_undirected()
    return nx.shortest_path_length(undirected_graph, orbit_a, orbit_b)


def main():
    input_txt = utils.get_input(6)
    p1 = part1(input_txt)
    x = 'YOU'
    y = 'SAN'
    p2 = part2(input_txt, x, y)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
