#!/usr/bin/env python

from utils import utils
import re
import networkx as nx


class Tree(object): 
    def __init__(self, root, G):
        self.root = root
        self.graph = G
        self.shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))
        # print(self.shortest_path_lengths)
        self.levels = self.get_max()
        # print(self.levels)
        print(self.get_nodes_of_level(1))
        # self.levels = max(self.shortest_path_lengths.values)

    def get_max(self) -> int:
        max_v = 0
        for i in self.shortest_path_lengths:
            for j in self.shortest_path_lengths[i]:
                if self.shortest_path_lengths[i][j] > max_v:
                    max_v = self.shortest_path_lengths[i][j]
        return max_v

    def get_nodes_of_level(self, level: int) -> list:
        nodes = []
        for x in self.shortest_path_lengths[self.root].keys():
            if self.shortest_path_lengths[self.root][x] == level:
                nodes.append(x)
        return nodes

    def get_direct_siblings(self, node: str) -> set:
        siblings = set()
        parents = list(self.graph.predecessors(node))
        if len(parents) != 1:
            return None
        edges = self.graph.out_edges(parents[0])
        siblings = {child for parent, child in edges if child != node}
        return siblings

    def get_cummulative_child_weights(self, node: str) -> int:
        out_edges = self.graph.out_edges(node)
        children = [child for parent, child in out_edges]
        return sum([self.graph.node[child]['weight'] for child in children])


    def is_node_balanced(self, node: str) -> bool:
        siblings = self.get_direct_siblings(node)
        for sibling in siblings:
            if self.get_cummulative_child_weights(node) != self.get_cummulative_child_weights(sibling):
                return False
        return True

    def find_unbalanced_node(self):
        for i in range(self.levels + 1):
            break
        pass


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

        # print('line:', line)
    # print(tree.nodes)
    root = list(nx.topological_sort(tree))[0]
    print(root)
    my_tree = Tree(root, tree)
    print(my_tree.graph.node['nbyij'])


def main():
    part_one(7)


if __name__ == '__main__':
    main()