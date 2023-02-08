#!/usr/bin/env python

from collections import deque

from utils import utils

"""
Code for https://adventofcode.com/2022/day/23
"""

neighbors = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
north = [(-1, -1), (0, -1), (1, -1)]
south = [(-1, 1), (0, 1), (1, 1)]
west = [(-1, -1), (-1, 0), (-1, 1)]
east = [(1, -1), (1, 0), (1, 1)]


def n_move(pos, elf, elves):
    if all(utils.tuple_add(pos, n) not in elves for n in north):
        elf.proposed = utils.tuple_add(pos, (0, -1))
        return True
    return False


def s_move(pos, elf, elves):
    if all(utils.tuple_add(pos, n) not in elves for n in south):
        elf.proposed = utils.tuple_add(pos, (0, 1))
        return True
    return False


def w_move(pos, elf, elves):
    if all(utils.tuple_add(pos, n) not in elves for n in west):
        elf.proposed = utils.tuple_add(pos, (-1, 0))
        return True
    return False


def e_move(pos, elf, elves):
    if all(utils.tuple_add(pos, n) not in elves for n in east):
        elf.proposed = utils.tuple_add(pos, (1, 0))
        return True
    return False


class Elf:
    def __init__(self, proposed=None):
        self.proposed = proposed


def move(elves, moves):
    # first half - check for neighbors and set proposed pos
    for k, v in elves.items():
        no_neighbors = all(utils.tuple_add(k, n) not in elves for n in neighbors)
        if no_neighbors:
            v.proposed = None
            continue
        for m in moves:
            if m(k, v, elves):
                break
    # second half - move if unique proposed pos
    new_elves = {}
    moved = False
    for k, v in elves.items():
        if not v.proposed:
            new_elves[k] = v
            continue
        moved = True
        same_proposed = [(pos, elf) for pos, elf in elves.items() if elf.proposed == v.proposed]
        if len(same_proposed) == 1:
            new_elves[v.proposed] = v
            v.proposed = None
        else:
            for pos, elf in same_proposed:
                elf.proposed = None
                new_elves[pos] = elf

    return new_elves, moved


def print_elves_only(elves):
    max_x = max([x for x, y in elves.keys()])
    min_x = min([x for x, y in elves.keys()])
    max_y = max([y for x, y in elves.keys()])
    min_y = min([y for x, y in elves.keys()])
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in elves:
                line += "#"
            else:
                line += "."
        print(line)


def count_empy_tiles(elves):
    max_x = max([x for x, y in elves.keys()])
    min_x = min([x for x, y in elves.keys()])
    max_y = max([y for x, y in elves.keys()])
    min_y = min([y for x, y in elves.keys()])
    empty_tiles = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) not in elves:
                empty_tiles += 1
    return empty_tiles


def main():
    input_txt = utils.get_input(23)

    moves = deque([n_move, s_move, w_move, e_move])
    elves = {}

    for y, line in enumerate(input_txt.split("\n")):
        for x, c in enumerate(line):
            if c == "#":
                elves[x, y] = Elf()

    for idx in range(1, int(1e7)):
        elves, moved = move(elves, moves)
        if not moved:
            print(f"Part 2: {idx}")
            break
        if idx == 11:
            print(f"Part 1: {count_empy_tiles(elves)}")
        # cycle priority of moves
        moves.rotate(-1)


if __name__ == "__main__":
    main()
