#!/usr/bin/env python

from utils import utils
from copy import copy

all_possibilities = list()


def get_max(current_state: list, value: int, available: set) -> None:

    if available:
        for node in available:
            if node[0] == value:
                then_available = copy(available)
                then_available.remove(node)
                here_current_state = copy(current_state)
                here_current_state.append(node)
                all_possibilities.append(here_current_state)
                get_max(here_current_state, node[-1], then_available)

            elif node[-1] == value:
                then_available = copy(available)
                then_available.remove(node)
                here_current_state = copy(current_state)
                here_current_state.append(node)
                all_possibilities.append(here_current_state)
                get_max(here_current_state, node[0], then_available)


def main():
    components = [cp for cp in utils.get_input(24).strip().split('\n')]

    available = set()
    global all_possibilities
    all_possibilities = list()

    for cp in components:
        port_a, port_b = [int(x) for x in cp.strip().split('/')]
        available.add((port_a, port_b))

    for bridge in available:
        if bridge[0] == 0:
            tmp = copy(available)
            tmp.remove(bridge)
            get_max([bridge], bridge[-1], tmp)
        elif bridge[-1] == 0:
            tmp = copy(available)
            tmp.remove(bridge)
            get_max([bridge], bridge[0], tmp)

    maximum = max([sum([t[0] + t[-1] for t in xs]) for xs in all_possibilities])
    print('Part 1: ', maximum)

    longest = max(all_possibilities, key=lambda x: len(x))
    print('Part 2: ', sum([x[0] + x[-1] for x in longest]))


if __name__ == '__main__':
    main()
