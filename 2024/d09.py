#!/usr/bin/env python

from copy import copy
from typing import Union

from utils import utils

type Disk = list[Union[int, str]]


def compact_disk(disk: Disk) -> None:
    n = len(disk)
    left, right = 0, n - 1

    while left < right:
        while left < n and disk[left] != ".":
            left += 1
        if left >= right:
            break

        while right > left and disk[right] == ".":
            right -= 1

        if disk[right] != ".":
            disk[left], disk[right] = disk[right], "."
            left += 1
            right -= 1


def find_file_blocks(disk: Disk) -> dict[int, tuple[int, int]]:
    blocks = {}
    start = 0
    curr_id = disk[0]

    for i in range(1, len(disk)):
        if disk[i] != curr_id:
            if curr_id != ".":
                blocks[curr_id] = (start, i - 1)
            start = i
            curr_id = disk[i]

    if curr_id != ".":
        blocks[curr_id] = (start, len(disk) - 1)

    return blocks


def compact_disk2(disk: Disk) -> None:
    file_blocks = find_file_blocks(disk)
    max_id = max(file_blocks.keys(), default=-1)

    for file_id in range(max_id, -1, -1):
        if file_id not in file_blocks:
            continue

        block_start, block_end = file_blocks[file_id]
        block_size = block_end - block_start + 1
        free_start = -1
        free_count = 0

        for i in range(block_start):
            if disk[i] == ".":
                if free_start == -1:
                    free_start = i
                free_count += 1
                if free_count >= block_size:
                    break
            else:
                free_start = -1
                free_count = 0

        if free_count >= block_size:
            disk[free_start : free_start + block_size] = disk[
                block_start : block_end + 1
            ]
            disk[block_start : block_end + 1] = ["."] * block_size


def calculate_checksum(disk: Disk) -> int:
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id != ".")


def part1(disk: Disk) -> int:
    compact_disk(disk)
    return calculate_checksum(disk)


def part2(disk: Disk) -> int:
    compact_disk2(disk)
    return calculate_checksum(disk)


def main() -> None:
    input_txt = utils.get_input(9)
    disk_map = [int(c) for c in input_txt]

    disk = []
    file_lengths = disk_map[0::2]
    free_spaces = disk_map[1::2]

    for i, length in enumerate(file_lengths):
        disk.extend([i] * length)
        if i < len(free_spaces):
            disk.extend(["."] * free_spaces[i])
    disk2 = copy(disk)

    print(f"Part1: {part1(disk)}")
    print(f"Part2: {part2(disk2)}")


if __name__ == "__main__":
    main()
