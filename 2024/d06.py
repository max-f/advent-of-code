#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2024/day/6
"""

MOVE = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0)
}


def part1(grid, starting_pos) -> int:
    visited = set()

    max_y = max(y for y, _ in grid.keys())
    max_x = max(x for _, x in grid.keys())
    curr = starting_pos
    guard = grid[starting_pos]

    while True:
        visited.add(curr)
        next_move = MOVE[guard]
        next_pos = utils.tuple_add(curr, next_move)
        if next_pos[0] < 0 or next_pos[0] > max_y or next_pos[1] < 0 or next_pos[1] > max_x:
            break
        if grid[next_pos] == "#":
            match guard:
                case "^":
                    guard = ">"
                case ">":
                    guard = "v"
                case "v":
                    guard = "<"
                case "<":
                    guard = "^"
            continue
        else:
            curr = next_pos

    return len(visited)


def is_in_grid(t: tuple[int, int], max_y, max_x):
    return 0 <= t[0] <= max_y and 0 <= t[1] <= max_x


def part2(grid, starting_pos):
    answer = 0

    max_y = max(y for y, _ in grid.keys())
    max_x = max(x for _, x in grid.keys())

    for m in grid.keys():
        if grid[m] != ".":
            continue

        grid[m] = "#"
        visited = set()

        curr = starting_pos
        guard = grid[starting_pos]

        while True:
            visited.add((curr, guard))
            next_move = MOVE[guard]
            next_pos = utils.tuple_add(curr, next_move)
            if not is_in_grid(next_pos, max_y, max_x):
                break
            if grid[next_pos] == "#":
                match guard:
                    case "^":
                        guard = ">"
                    case ">":
                        guard = "v"
                    case "v":
                        guard = "<"
                    case "<":
                        guard = "^"
                continue
            else:
                curr = next_pos
                if (curr, guard) in visited:
                    answer += 1
                    break
        grid[m] = "."
    return answer


def main():
    input_txt = utils.get_input(6)
    grid = {}
    starting_pos = (-1, -1)
    for i, line in enumerate(input_txt.split("\n")):
        for j, c in enumerate(line):
            if c == "^":
                starting_pos = (i, j)
            grid[i, j] = c

    print(f"Part1: {part1(grid, starting_pos)}")
    print(f"Part2: {part2(grid, starting_pos)}")


if __name__ == "__main__":
    main()
