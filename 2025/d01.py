#!/usr/bin/env python
from utils import utils

"""
Code for https://adventofcode.com/2025/day/1
"""


def parse_move(move: str) -> tuple[int, int]:
    direction = -1 if move[0] == "L" else 1
    steps = int(move[1:])
    return direction, steps


def update_position(position: int, direction: int, steps: int) -> int:
    return (position + direction * steps) % 100


def count_crossings(position: int, direction: int, steps: int) -> int:
    full_rotations = steps // 100
    remaining = steps % 100

    crosses_zero = 0
    if direction == -1 and remaining > position > 0:
        crosses_zero = 1
    elif direction == 1 and position + remaining > 100:
        crosses_zero = 1

    return full_rotations + crosses_zero


def solve(start: int, moves: list[str], count_passes: bool) -> int:
    position = start
    total = 0

    for move in moves:
        direction, steps = parse_move(move)

        if count_passes:
            total += count_crossings(position, direction, steps)

        position = update_position(position, direction, steps)
        total += position == 0

    return total


def part1(start: int, moves: list[str]) -> int:
    return solve(start, moves, False)


def part2(start: int, moves: list[str]) -> int:
    return solve(start, moves, True)


def parse_input(input_txt: str) -> list[str]:
    return input_txt.strip().split()


def main():
    input_txt = utils.get_input(1)
    moves = parse_input(input_txt)
    print(f"Part1: {part1(50, moves)}")
    print(f"Part2: {part2(50, moves)}")


if __name__ == "__main__":
    main()
