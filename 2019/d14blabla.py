#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from utils.utils import get_input, ints, tuple_add
import re
import networkx as nx
from fractions import Fraction
import math
from pprint import pprint


def calc_amount(required_amount, step):
    required_amount = math.ceil(required_amount)
    while required_amount % step != 0:
        required_amount += 1
    return required_amount


def backtrack(G, amount):
    chem_store = defaultdict(int)

    def produce(chem: str, required_amount):
        if chem == 'ORE':
            chem_store[chem] += required_amount
            return
        elif chem_store[chem] >= required_amount:
            chem_store[chem] -= required_amount
            return
        else:
            required_amount = required_amount - chem_store[chem]
            predecessors = G.predecessors(chem)
            for pre in predecessors:
                e_weight = G[pre][chem]['weight']
                current_step = G[pre][chem]['step']
                required_pre_amount = calc_amount(e_weight * required_amount, current_step)
                produce(pre, required_pre_amount)
                chem_store[chem] = (e_weight * current_step) - required_amount

    produce('FUEL', amount)

    # Debug
    pprint(chem_store)

    return chem_store

def main():
    input_txt = get_input(54)

    G = nx.DiGraph()

    chemical_re = re.compile(r'(\d+) (\w+)')
    for line in input_txt.strip().split('\n'):
        pre, post = line.split('=>')
        pre_chemicals = chemical_re.findall(pre)
        post = chemical_re.findall(post)

        if len(post) > 1:
            raise ValueError(f'Multiple chemicals as reaction product? -> {post}')

        post_number, post_name = post[0]

        for number, name in pre_chemicals:
            node1 = name
            node2 = post_name
            # edge_weight = Fraction(int(post_number), int(number))
            edge_weight = Fraction(int(number), int(post_number))
            step = int(post_number)
            G.add_edge(node1, node2, weight=edge_weight, step=step)

    backtrack(G, 1)


if __name__ == "__main__":
    main()
