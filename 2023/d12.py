#!/usr/bin/env python

import functools

from utils import utils

"""
Code for https://adventofcode.com/2023/day/12
"""


@functools.lru_cache
def recursive_count(cfg: str, nums: tuple[int, ...]) -> int:
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0
    if cfg[0] in ".?":
        result += recursive_count(cfg[1:], nums)

    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += recursive_count(cfg[nums[0] + 1 :], nums[1:])

    return result


def main():
    input_txt = utils.get_input(12)
    lines = input_txt.strip().split("\n")

    total_p1 = 0
    total_p2 = 0
    for line in lines:
        spring_config, numbers = line.split(" ")
        nums = tuple(utils.ints(numbers))
        total_p1 += recursive_count(spring_config, nums)

        extended_spring_cfg = "?".join([spring_config] * 5)
        total_p2 += recursive_count(extended_spring_cfg, nums * 5)

    print(f"Part 1: {total_p1}")
    print(f"Part 2: {total_p2}")


if __name__ == "__main__":
    main()
