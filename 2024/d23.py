#!/usr/bin/env python

from utils import utils
import networkx as nx
from itertools import combinations


def count_triangles_with_t(triangles):
    return sum(
        1 for triangle in triangles if any(comp.startswith("t") for comp in triangle)
    )


def find_triangles(G):
    triangles = []
    nodes = list(G.nodes())

    for three_nodes in combinations(nodes, 3):
        if all(
            G.has_edge(three_nodes[i], three_nodes[j])
            for i, j in combinations(range(3), 2)
        ):
            triangles.append(sorted(three_nodes))

    return triangles


def find_largest_clique(G):
    cliques = list(nx.find_cliques(G))
    return max(cliques, key=len)


def part1(G):
    triangles = find_triangles(G)
    t_count = count_triangles_with_t(triangles)
    return t_count


def part2(G):
    largest_clique = find_largest_clique(G)
    largest_clique.sort()
    return ",".join(largest_clique)


def build_graph(input_txt: str):
    G = nx.Graph()
    for line in input_txt.strip().split("\n"):
        a, b = line.split("-")
        G.add_edge(a, b)
    return G


def main() -> None:
    input_txt = utils.get_input(23)
    G = build_graph(input_txt)
    print(f"Part1: {part1(G)}")
    print(f"Part2: {part2(G)}")


if __name__ == "__main__":
    main()
