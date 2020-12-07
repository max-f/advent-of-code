#!/usr/bin/env python

import re
from utils import utils
import networkx as nx

"""
Code for https://adventofcode.com/2020/day/7
"""


def part1(G: nx.DiGraph) -> int:
    return len(nx.ancestors(G, "shiny gold"))


def part2(G: nx.DiGraph) -> int:
    return add_stuff(G, "shiny gold", 1)


def add_stuff(G: nx.DiGraph, source: str, necessary_amount: str) -> int:
    successors = G.successors(source)
    total = 0
    for successor in successors:
        new_necessary = necessary_amount * G[source][successor]["weight"]
        total += new_necessary
        total += add_stuff(G, successor, new_necessary)
    return total


def main():
    input_txt = utils.get_input(7).rstrip()
    G = nx.DiGraph()
    for line in input_txt.split("\n"):
        if "no other" in line:
            continue
        current_color = re.match(r"^(\w+ \w+).+$", line).group(1)
        out_edges = re.findall(r"(\d+ \w+ \w+)", line)
        for out in out_edges:
            number, color = out.split(" ", 1)
            G.add_edge(current_color, color, weight=int(number))

    print(part1(G))
    print(part2(G))


if __name__ == "__main__":
    main()
