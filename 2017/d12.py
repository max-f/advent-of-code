#!/usr/bin/env python

import networkx as nx

from utils import utils


# Using networkX :x

def build_graph(day: int) -> None:
    G = nx.Graph()

    input_str = utils.get_input(day)
    for line in input_str.rstrip().split('\n'):
        a, bs = line.split('<->')
        a = a.rstrip()
        bs = bs.split(',')
        bs = [b.strip() for b in bs]
        for b in bs:
            G.add_edge(a, b)

    conn_component = nx.node_connected_component(G, '0')
    print(len(conn_component))
    print(nx.number_connected_components(G))


def main():
    build_graph(12)


if __name__ == '__main__':
    main()
