#!/usr/bin/env python

import re

from utils import utils

"""
Code for https://adventofcode.com/2021/day/17
"""


def part1(target_area) -> int:
    max_y = 0

    for x in range(300):
        for y in range(300):
            velocity = [x, y]
            pos_x, pos_y = [0, 0]
            tmp_max_y = 0
            hit_target = False
            for _ in range(600):
                pos_x += velocity[0]
                pos_y += velocity[1]

                if velocity[0] > 0:
                    velocity[0] -= 1
                elif velocity[0] < 0:
                    velocity[0] += 1
                velocity[1] -= 1
                if (pos_x, pos_y) in target_area:
                    hit_target = True
                    break
                if pos_y > tmp_max_y:
                    tmp_max_y = pos_y
            if hit_target and tmp_max_y > max_y:
                max_y = tmp_max_y
    return max_y


def part2(target_area) -> int:
    velocities = []

    for x in range(-250, 250):
        for y in range(-250, 250):
            velocity = [x, y]
            old_velocity = [x, y]
            pos_x, pos_y = [0, 0]
            hit_target = False
            for _ in range(600):
                pos_x += velocity[0]
                pos_y += velocity[1]

                if velocity[0] > 0:
                    velocity[0] -= 1
                elif velocity[0] < 0:
                    velocity[0] += 1
                velocity[1] -= 1
                if (pos_x, pos_y) in target_area:
                    hit_target = True
                    break

            if hit_target:
                velocities.append(old_velocity)
    return len(velocities)


def main():
    input_txt = utils.get_input(17)
    regex = re.compile(r".*x=(-?\d+)..(-?\d+).*y=(-?\d+)..(-?\d+)")
    match = regex.match(input_txt)
    tx1, tx2, ty1, ty2 = (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
        int(match.group(4)),
    )
    target_area = set()
    for x in range(tx1, tx2 + 1):
        for y in range(ty1, ty2 + 1):
            target_area.add((x, y))

    print(f"Part 1: {part1(target_area)}")
    print(f"Part 2: {part2(target_area)}")


if __name__ == "__main__":
    main()
