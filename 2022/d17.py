#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/17
"""

move_dict = {">": (1, 0), "<": (-1, 0)}

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
]

TOTAL_ROCKS = 2022
CHAMBER_WIDTH = 7


def part1(sensors, beacons):
    pass


def part2():
    pass


def main():
    input_txt = utils.get_input(17).strip()
    movements = list(input_txt)

    # {(x1, y1), (x2, y2), ...}
    all_resting = set()

    rock_counter = 0
    movement_idx = 0

    # next rock
    while rock_counter < TOTAL_ROCKS:
        # Find next rock shape which will be stacked and move it to its starting position
        moving_rock = place_new_rock(shapes[rock_counter % 5], all_resting)
        falling = True

        while falling:
            # Get lateral move for this iteration and set up next one
            move: tuple = move_dict[movements[movement_idx]]
            movement_idx += 1
            movement_idx %= len(movements)
            # check if rock is laterally movable and move it if possible
            if is_lateral_move_valid(moving_rock, move, all_resting):
                moving_rock: list[tuple[int, int]] = [
                    utils.tuple_add(coord, move) for coord in moving_rock
                ]

            # check if rock is downward movable and move it if possible
            # else add rock to resting rocks and stop falling state to place next rock
            if is_down_move_valid(moving_rock, all_resting):
                moving_rock: list[tuple[int, int]] = [
                    utils.tuple_add(coord, (0, -1)) for coord in moving_rock
                ]
            else:
                falling = False
                all_resting.update(moving_rock)

        rock_counter += 1

    max_y = max(all_resting, key=lambda x: x[1])[1] + 1
    print(f"Part 1: {max_y}")


def place_new_rock(
    rock: list[tuple[int, int]], resting: set[tuple[int, int]]
) -> list[tuple[int, int]]:
    if not resting:
        max_y = -1
    else:
        max_y = max([coord[-1] for coord in resting])
    # left edge two units away from left wall
    # lower edge three units away from ground or resting rock
    rock = [(x + 2, y + max_y + 4) for (x, y) in rock]
    return rock


def is_lateral_move_valid(
    rock: list[tuple[int, int]], move: tuple[int, int], resting: set[tuple[int, int]]
) -> bool:
    in_chamber_width = all(0 <= x + move[0] < CHAMBER_WIDTH for x, y in rock)
    no_collision = all((x + move[0], y) not in resting for x, y in rock)
    return in_chamber_width and no_collision


def is_down_move_valid(
    rock: list[tuple[int, int]], resting: set[tuple[int, int]]
) -> bool:
    above_ground = all(0 <= y - 1 for x, y in rock)
    no_collision = all((x, y - 1) not in resting for x, y in rock)
    return above_ground and no_collision


def print_map(
    all_resting: set[tuple[int, int]], moving_rock: list[tuple[int, int]] = None
) -> None:
    if moving_rock:
        max_y_set = all_resting.union(moving_rock)
    else:
        max_y_set = all_resting
    max_y = max(max_y_set, key=lambda x: x[1])[1]
    for y in range(max_y, -1, -1):
        for x in range(CHAMBER_WIDTH):
            if all_resting and (x, y) in all_resting:
                print("#", end="")
            elif moving_rock and (x, y) in moving_rock:
                print("@", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    main()
