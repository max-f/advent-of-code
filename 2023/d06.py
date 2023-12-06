#!/usr/bin/env python

import math
from itertools import count

from utils import utils

"""
Code for https://adventofcode.com/2023/day/6
"""


def part1(races: list[tuple[int, int]]) -> int:
    results = [calculate_ways_to_win(time, distance) for time, distance in races]
    return math.prod(results)


def part2(time, distance) -> int:
    return calculate_ways_to_win(time, distance)


def calculate_ways_to_win(time: int, distance: int) -> int:
    result = 0

    for t in count():
        speed = t
        if t > time:
            break
        else:
            if speed * (time - t) > distance:
                result += 1
    return result


def main():
    input_txt = utils.get_input(6)
    time, distance = input_txt.strip().split("\n")
    times = utils.ints(time)
    distances = utils.ints(distance)
    races = zip(times, distances)

    time2 = int(''.join([time.strip() for time in time.split(" ")[1:]]))
    distance2 = int(''.join([distance.strip() for distance in distance.split(" ")[1:]]))

    print(f"Part1: {part1(races)}")
    print(f"Part2: {part2(time2, distance2)}")


if __name__ == "__main__":
    main()
