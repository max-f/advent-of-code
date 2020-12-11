#!/usr/bin/env python

from utils import utils
from functools import lru_cache

"""
Code for https://adventofcode.com/2020/day/11
"""

MAX_X = 0
MAX_Y = 0
DIRS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def part1(occupied: set[tuple[int, int]], empty: set[tuple[int, int]]) -> int:
    while True:
        getting_occupied = check_empty(occupied, empty)
        getting_empty = check_occupied(occupied)
        if not getting_occupied and not getting_empty:
            break
        occupied = (occupied | getting_occupied) - getting_empty
        empty = (empty | getting_empty) - getting_occupied
    return len(occupied)


def part2(occupied: set[tuple[int, int]], empty: set[tuple[int, int]]) -> int:
    while True:
        getting_occupied = check_empty2(occupied, empty)
        getting_empty = check_occupied2(occupied, empty)
        if not getting_occupied and not getting_empty:
            break
        occupied = (occupied | getting_occupied) - getting_empty
        empty = (empty | getting_empty) - getting_occupied
    return len(occupied)


def check_empty2(
    occupied: set[tuple[int, int]], empty: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    getting_occupied = set()
    for pos in empty:
        occupied_adjacent = calculate_viewable_occupied(pos, occupied, empty)
        if occupied_adjacent == 0:
            getting_occupied.add(pos)
    return getting_occupied


def check_occupied2(
    occupied: set[tuple[int, int]], empty: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    getting_empty = set()
    for pos in occupied:
        occupied_adjacent = calculate_viewable_occupied(pos, occupied, empty)
        if occupied_adjacent >= 5:
            getting_empty.add(pos)
    return getting_empty


def calculate_viewable_occupied(
    pos: tuple[int, int], occupied: set[tuple[int, int]], empty: set[tuple[int, int]]
) -> int:
    global DIRS

    adjacent_occupied = 0
    for dir_ in DIRS:
        if has_occupied_seat_in_direction(pos, dir_, occupied, empty):
            adjacent_occupied += 1
    return adjacent_occupied


def has_occupied_seat_in_direction(
    pos: tuple[int, int],
    direction: tuple[int, int],
    occupied: set[tuple[int, int]],
    empty: set[tuple[int, int]],
):
    new_x, new_y = utils.tuple_add(pos, direction)
    if new_x < 0 or new_x > MAX_X or new_y < 0 or new_y > MAX_Y:
        return None
    elif (new_x, new_y) in empty:
        return False
    elif (new_x, new_y) in occupied:
        return True
    else:
        return has_occupied_seat_in_direction((new_x, new_y), direction, occupied, empty)


@lru_cache(maxsize=None)
def calculate_adjacent(pos: tuple[int, int]) -> set[tuple[int, int]]:
    return {utils.tuple_add(pos, dir_) for dir_ in DIRS}


def check_empty(occupied, empty):
    getting_occupied = set()
    for seat in empty:
        adjacent = calculate_adjacent(seat)
        occupied_adjacent = len(occupied & adjacent)
        if not occupied_adjacent:
            getting_occupied.add(seat)
    return getting_occupied


def check_occupied(occupied):
    getting_empty = set()
    for seat in occupied:
        adjacent = calculate_adjacent(seat)
        occupied_adjacent = len(occupied & adjacent)
        if occupied_adjacent >= 4:
            getting_empty.add(seat)
    return getting_empty


def main():
    input_txt = utils.get_input(11).rstrip()
    empty = set()
    floor = set()
    occupied = set()
    lines = input_txt.split("\n")
    global MAX_X
    global MAX_Y
    MAX_X = len(lines[0])
    MAX_Y = len(lines) - 1

    for y, line in enumerate(lines):
        row = list(line)
        for x, pos in enumerate(row):
            if pos == "L":
                empty.add((x, y))
            elif pos == ".":
                floor.add((x, y))

    print(part1(occupied, empty))
    print(part2(occupied, empty))


if __name__ == "__main__":
    main()
