#!/usr/bin/env python

import re

import networkx as nx

from utils import utils


class Tree(object):
    def __init__(self, root, G):
        self.root = root
        self.graph = G
        self.shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))
        self.levels = self.get_max()

    def get_max(self) -> int:
        max_v = 0
        for i in self.shortest_path_lengths:
            for j in self.shortest_path_lengths[i]:
                if self.shortest_path_lengths[i][j] > max_v:
                    max_v = self.shortest_path_lengths[i][j]
        return max_v

    def get_nodes_of_level(self, level: int) -> set:
        nodes = set()
        for x in self.shortest_path_lengths[self.root].keys():
            if self.shortest_path_lengths[self.root][x] == level:
                nodes.add(x)
        return nodes

    def get_all_siblings(self, node: str) -> list:
        parents = list(self.graph.predecessors(node))
        if len(parents) != 1:
            return None
        edges = self.graph.out_edges(parents[0])
        siblings = [child for parent, child in edges]
        return siblings

    def get_cummulative_child_weight(self, node: str) -> int:
        out_edges = self.graph.out_edges(node)
        children = [child for parent, child in out_edges]
        return sum([self.graph.node[child]['cweight'] for child in children])

    def find_unbalanced_sibling(self, siblings: list):
        sibling_weights = [self.graph.node[sibling]['cweight'] for sibling in siblings]
        max_weight = max(sibling_weights)
        min_weight = min(sibling_weights)
        if not all(w == max_weight for w in sibling_weights):
            if sibling_weights.count(max_weight) > sibling_weights.count(min_weight):
                idx = sibling_weights.index(min_weight)
            else:
                idx = sibling_weights.index(max_weight)
            return siblings[idx]
        return None

    def find_unbalanced_node(self) -> None:
        for i in reversed(range(self.levels + 1)):
            lvl_nodes = self.get_nodes_of_level(i)
            visited = set()

            for node in lvl_nodes:
                self.graph.node[node]['cweight'] = self.graph.node[node]['weight'] \
                                                   + self.get_cummulative_child_weight(node)

            for node in lvl_nodes:
                if node in visited:
                    continue
                siblings = self.get_all_siblings(node)
                unbalanced_sibling = self.find_unbalanced_sibling(siblings)
                if not unbalanced_sibling:
                    visited = visited | set(siblings)
                else:
                    self.print_diff(siblings, unbalanced_sibling)
                    return

    def print_diff(self, siblings: list, unbalanced_node: object) -> None:
        bad_idx = siblings.index(unbalanced_node)
        if bad_idx == 0:
            good_sibling = siblings[-1]
        else:
            good_sibling = siblings[0]
        diff = self.graph.node[unbalanced_node]['cweight'] - self.graph.node[good_sibling]['cweight']
        if diff < 0:
            print('Node {0} needs a weight of {1}'.format(unbalanced_node,
                                                          self.graph.node[unbalanced_node]['weight']
                                                          + diff))
        else:
            print('Node {0} needs a weight of {1}'.format(unbalanced_node,
                                                          self.graph.node[unbalanced_node]['weight']
                                                          - diff))


def part_one(day: int) -> None:
    tree = nx.DiGraph()
    edges = list()

    node_pattern = r'(\w+) \((\d+)\).*'
    std_regex = re.compile(node_pattern)

    input_str = utils.get_input(day)
    for line in input_str.split('\n'):
        splitted_line = line.split('->')
        match = std_regex.match(splitted_line[0])
        if match:
            node, weight = match.group(1), match.group(2)
            tree.add_node(node, weight=int(weight))

            if len(splitted_line) > 1:
                children = [s.rstrip(',') for s in splitted_line[1].split()]
                for child in children:
                    edges.append((node, child))
    tree.add_edges_from(edges)

    root = list(nx.topological_sort(tree))[0]
    print('Root:', root)
    my_tree = Tree(root, tree)
    my_tree.find_unbalanced_node()


def main():
    part_one(7)


if __name__ == '__main__':
    main()
