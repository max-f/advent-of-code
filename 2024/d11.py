#!/usr/bin/env python

from utils import utils
from collections import defaultdict


def step(stones: dict[int, int]) -> dict[int, int]:
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
            continue

        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            mid = len(stone_str) // 2
            left = int(stone_str[:mid])
            right = int(stone_str[mid:])
            new_stones[left] += count
            new_stones[right] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones


def part1(stones: list[int], steps) -> int:
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in range(steps):
        stone_counts = step(stone_counts)
    return sum(stone_counts.values())


def part2(stones: list[int], steps) -> int:
    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] += 1

    for _ in range(steps):
        stone_counts = step(stone_counts)
    return sum(stone_counts.values())


def main() -> None:
    input_txt = utils.get_input(11)

    stones = utils.ints(input_txt)

    print(f"Part1: {part1(stones, 25)}")
    print(f"Part2: {part2(stones, 75)}")


if __name__ == "__main__":
    main()
