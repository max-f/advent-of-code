#!/usr/bin/env python

import math
import re

from utils import utils

"""
Code for https://adventofcode.com/2023/day/2
"""


def part1(lines: list[str]) -> int:
    limit = {"red": 12, "green": 13, "blue": 14}
    valid_games = []
    for game_id, line in enumerate(lines):
        valid = True
        game_configs = line.split(";")
        for game_config in game_configs:
            balls = re.findall(r"(\d+) (blue|red|green)", game_config)
            if any([int(ball[0]) > limit[ball[1]] for ball in balls]):
                valid = False
                break
        if valid:
            valid_games.append(game_id + 1)
    return sum(valid_games)


def part2(lines: list[str]) -> int:
    all_powers = []
    for game_id, line in enumerate(lines):
        minimal_config = {"red": 0, "green": 0, "blue": 0}
        game_configs = line.split(";")
        for game_config in game_configs:
            balls = re.findall(r"(\d+) (blue|red|green)", game_config)
            for ball in balls:
                minimal_config[ball[1]] = max(int(ball[0]), minimal_config[ball[1]])
        all_powers.append(math.prod(minimal_config.values()))
    return sum(all_powers)


def main():
    input_txt = utils.get_input(2)
    lines = input_txt.strip().split("\n")

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
