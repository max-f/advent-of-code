#!/usr/bin/env python

from collections import defaultdict

from utils import utils
import networkx as nx
from pprint import pprint
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
    maximal_cliques = list(nx.find_cliques(G))
    max_size = len(max(maximal_cliques, key=len))
    largest_cliques = [clique for clique in maximal_cliques if len(clique) == max_size]
    largest_cliques = [sorted(clique) for clique in largest_cliques]
    largest_cliques.sort()
    return largest_cliques[0]

def part1(G):
    triangles = find_triangles(G)
    t_count = count_triangles_with_t(triangles)
    return t_count

def part2(G):
    largest_clique = find_largest_clique(G)
    return(','.join(largest_clique))


def main() -> None:
    input_txt = utils.get_input(23)
    G = nx.Graph()
    for line in input_txt.strip().split("\n"):
        a, b = line.split("-")
        G.add_edge(a, b)
    print(f"Part1: {part1(G)}")
    print(f"Part2: {part2(G)}")


if __name__ == "__main__":
    main()
