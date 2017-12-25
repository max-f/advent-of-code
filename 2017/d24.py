#!/usr/bin/env python

from collections import defaultdict
from utils import utils
from copy import copy

components = [cp for cp in utils.get_input(24).strip().split('\n')]

cps = dict()
available = set()
all_possibilites = list()


def get_max(current_state: list, value: int, available: set) -> None:

    if available:
        for node in available:
            if node[0] == value:
                then_available = copy(available)
                then_available.remove(node)
                here_current_state = copy(current_state)
                here_current_state.append(node)
                all_possibilites.append(here_current_state)
                get_max(here_current_state, node[-1], then_available)

            elif node[-1] == value:
                then_available = copy(available)
                then_available.remove(node)
                here_current_state = copy(current_state)
                here_current_state.append(node)
                all_possibilites.append(here_current_state)
                get_max(here_current_state, node[0], then_available)

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

longest = max(all_possibilites, key=lambda x: len(x))
print(len(longest))
print(sum([x[0] + x[-1] for x in longest]))

maximum = 0
for path in all_possibilites:
    path_value = sum([x[0] + x[-1] for x in path])
    if path_value > maximum:
        maximum = path_value

print(maximum)
print(type(all_possibilites[0]))



# if __name__ == '__main__':
    # main()
