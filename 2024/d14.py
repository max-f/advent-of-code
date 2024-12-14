#!/usr/bin/env python

from collections import defaultdict
from math import prod

from utils import utils


class Robot:
    def __init__(self, start: tuple[int, int], velocity: tuple[int, int]):
        self.start = start
        self.pos = start
        self.velocity = velocity

    def __repr__(self):
        return f"Start: {self.start} - Pos: {self.pos} - Velocity: {self.velocity}"

    def position_at_time(self, t: int, max_x: int, max_y: int) -> tuple[int, int]:
        dx = (self.start[0] + self.velocity[0] * t) % max_x
        dy = (self.start[1] + self.velocity[1] * t) % max_y
        return dx, dy


def visualize_positions(positions: set[tuple[int, int]], max_x: int, max_y: int):
    grid = [["." for _ in range(max_x)] for _ in range(max_y)]
    for x, y in positions:
        grid[y][x] = "#"
    return "\n".join("".join(row) for row in grid)


def part1(max_x, max_y, robots: list[Robot]) -> int:
    x_border = max_x // 2
    y_border = max_y // 2

    def quadrant(x, y):
        if x < x_border:
            return 1 if y < y_border else 2
        elif x > x_border:
            return 3 if y < y_border else 4
        return -1

    positions = [r.position_at_time(100, max_x, max_y) for r in robots]

    quadrants = defaultdict(int)
    for pos in positions:
        q = quadrant(*pos)
        if q != -1:
            quadrants[q] += 1
    return prod(quadrants.values())


def is_christmas_tree(positions: set[tuple[int, int]]) -> bool:
    points_by_y = defaultdict(set)
    for x, y in positions:
        points_by_y[y].add(x)

    adjacent_row_counts = defaultdict(int)
    for y, x_values in points_by_y.items():
        adjacent_count = 0
        for x in x_values:
            # Check if there's a point directly adjacent (x ± 1)
            if (x + 1) in x_values or (x - 1) in x_values:
                adjacent_count += 1
        adjacent_row_counts[y] = adjacent_count

    sorted_items_max_adjacent = sorted(
        list(adjacent_row_counts.items()), key=lambda x: x[1]
    )
    # I compare 3rd and 4th rows with most adjacent robot pos due to the 'frame' rows of the picture
    return (sorted_items_max_adjacent[-3][1] > 14
            and sorted_items_max_adjacent[-3][1] == (sorted_items_max_adjacent[-4][1] + 2))


# Originally solved by:
# Printing out visualization
# $ uv run d14.py > tree_out.txt
# $ rg -C 60 '############################' tree_out.txt
# :S
def part2(max_x: int, max_y: int, robots: list[Robot]) -> int:
    for t in range(1, 10001):
        positions = set()
        for robot in robots:
            pos = robot.position_at_time(t, max_x, max_y)
            positions.add(pos)

        if is_christmas_tree(positions):
            return t
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
