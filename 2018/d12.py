#!/usr/bin/env python

from collections import defaultdict, deque
import operator
import re

from utils import utils

import numpy as np

GENERATIONS = 50000000000
#GENERATIONS = 20

def count_pots(pots):
    return sum([i - 5 for i, c in enumerate(pots) if c == '#'])


#def apply_rules(current_state_filled, already_done)

def main():
    data = utils.get_input(12).split('\n')[:-1]
    current_state = data[0].lstrip('initial state: ')
    rule_lines = data[2:]

    rules = dict()
    for rule in rule_lines:
        rule = rule.split(' => ')
        print(rule)
        rules[rule[0]] = rule[1]

    current_state_filled = '.' * 5 + current_state + '.' * 100
    print(current_state_filled)
    already_done = dict()
    current_idx = 0

    for gen in range(GENERATIONS):
        current_idx = gen
        new_state = list(current_state_filled)
        start = current_state_filled.find('#') - 2
        stop = current_state_filled.rfind('#') + 3
        for i in range(start, stop):
            pattern = current_state_filled[i - 2:i + 3]
            if pattern in rules:
                new_state[i] = rules[pattern]
            else:
                new_state[i] = '.'
        current_state_filled = ''.join(new_state)
        if current_state_filled in already_done:
            break
        already_done[current_state_filled] = gen
        #print(current_state_filled)
    print(already_done)
    repeated_gen = already_done[current_state_filled]
    circle_length = current_idx - repeated_gen
    print(circle_length)
    todo = GENERATIONS % circle_length
    for pots, gen in already_done.items():
        if gen == repeated_gen + todo:
            print(count_pots(pots))





    #grid = Grid(serial_number)
    #best_cell, max_power_lvl = grid.find_max(3)
    #print(f"Part 1: {best_cell}")

    #best_cell, best_size = grid.find_general_max()
    #print(f"Part 2: {best_cell[0]},{best_cell[1]},{best_size}")


if __name__ == "__main__":
    main()
