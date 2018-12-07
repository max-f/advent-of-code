#!/usr/bin/env python

from utils import utils
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(data):
    G = nx.DiGraph()
    for line in data:
        if line:
            line_parts = line.split(' ')
            G.add_edge(line_parts[1], line_parts[7])
    starting_nodes = list((node for node in G if G.in_degree(node) == 0))
    return G, starting_nodes


def find_order(G, starting_nodes):
    order = []
    visited = set()
    to_visit = starting_nodes
    skip = 0

    while len(to_visit) != 0:
        to_visit = sorted(list(set(to_visit)))
        i = skip
        node = to_visit[i]
        predecessors = set(G.predecessors(node))

        # print('node', node)
        # print('Pred.', predecessors)
        # print('vis', visited)
        # print(order)
        # print(to_visit)
        # print(i)
        # print('#' * 10)

        if node in visited:
            del to_visit[i]
            skip -= 1
            continue

        elif set(G.predecessors(node)).issubset(visited):
            order.append(node)
            visited.add(node)
            del to_visit[i]
            to_visit.extend(list(G.successors(node)))
            skip = 0

        else:
            skip += 1
            print('skip',skip)

    print(order)
    print(len(G.nodes))
    return order


def main():
    data = utils.get_input(7).split("\n")
    G, starting_node = create_graph(data)
    # nx.draw(G)
    # plt.show()
    order = find_order(G, starting_node)
    order_str = ''.join(order)
    print(order_str)

    # print(f"Part 1: {}")
    # print(f"Part 2: {}")


if __name__ == "__main__":
    main()
