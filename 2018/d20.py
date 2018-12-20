#!/usr/bin/env python

import networkx as nx

from utils import utils


def main():
    regex = utils.get_input(20).lstrip('^').rstrip('$')

    G = nx.Graph()
    x = 0
    y = 0
    stack = []

    for c in regex:
        if c == '(':
            stack.append((x, y))
        elif c == ')':
            x, y = stack.pop()
        elif c == '|':
            x, y = stack[-1]
        else:
            old_x, old_y = x, y
            if c == 'W':
                x -= 1
            elif c == 'E':
                x += 1
            elif c == 'N':
                y -= 1
            elif c == 'S':
                y += 1
            G.add_edge((old_x, old_y), (x, y))

    shortest_paths = nx.shortest_path_length(G, source=(0, 0))
    most_doors = max(shortest_paths.values())
    atleast_1000 = len([
        room_distance for room_distance in shortest_paths.values()
        if room_distance >= 1000
    ])

    print(f'Part 1: {most_doors}')
    print(f'Part 2: {atleast_1000}')


if __name__ == "__main__":
    main()
