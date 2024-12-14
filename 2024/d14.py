#!/usr/bin/env python

from collections import defaultdict
from math import prod
from pprint import pprint

from utils import utils


class Robot:
    def __init__(self, start: tuple[int, int], velocity: tuple[int, int]):
        self.start = start
        self.pos = start
        self.velocity = velocity

    def __repr__(self):
        return f"Start: {self.start} - Pos: {self.pos} - Velocity: {self.velocity}"


def visualize_positions(positions: set[tuple[int, int]], max_x: int, max_y: int):
    grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for x, y in positions:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)


def quadrant(robot, max_x, max_y):
    x_boarder = max_x // 2
    y_boarder = max_y // 2
    x, y = robot.pos
    if x < x_boarder:
        if y < y_boarder:
            return 1
        elif y > y_boarder:
            return 2
    elif x > x_boarder:
        if y < y_boarder:
            return 3
        elif y > y_boarder:
            return 4
    return -1


def part1(max_x, max_y, robots: list[Robot]) -> int:
    def step(robot: Robot):
        new_x = (robot.pos[0] + robot.velocity[0]) % max_x
        new_y = (robot.pos[1] + robot.velocity[1]) % max_y
        robot.pos = (new_x, new_y)

    for _ in range(100):
        for r in robots:
            step(r)

    quadrants = defaultdict(int)
    for r in robots:
        q = quadrant(r, max_x, max_y)
        if q != -1:
            quadrants[q] += 1
    pprint(quadrants)
    return prod(quadrants.values())


# Solved by:
# $ uv run d14.py > tree_out.txt
# $ rg -C 60 '############################' tree_out.txt
# :S
def part2(max_x: int, max_y: int, robots: list[Robot]) -> int:
    def step(robot: Robot):
        new_x = (robot.pos[0] + robot.velocity[0]) % max_x
        new_y = (robot.pos[1] + robot.velocity[1]) % max_y
        robot.pos = (new_x, new_y)

    for t in range(10000):
        for r in robots:
            step(r)
        occupied_positions = set([r.pos for r in robots])
        print(f"Step: {t + 1}")
        print(visualize_positions(occupied_positions, max_x, max_y) + "\n\n")

    return -1


def main() -> None:
    input_txt = utils.get_input(14)

    lines = input_txt.strip().split("\n")
    robots = []
    max_x = 101  # 101 / 11
    max_y = 103  # 103 / 7

    for line in lines:
        pos_x, pos_y, dx, dy = utils.ints(line)
        robot = Robot((pos_x, pos_y), (dx, dy))
        robots.append(robot)

    print(f"Part1: {part1(max_x, max_y, robots)}")
    print(f"Part2: {part2(max_x, max_y, robots)}")


if __name__ == "__main__":
    main()
