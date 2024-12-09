#!/usr/bin/env python

from utils import utils
from collections import deque
from copy import copy

"""
Code for https://adventofcode.com/2024/day/9
"""


def find_leftmost_space(disk):
    for i, val in enumerate(disk):
        if val == '.':
            return i
    return -1


def find_rightmost_file(disk):
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != '.':
            return i
    return -1


def compact_disk(disk):
    while True:
        space_pos = find_leftmost_space(disk)
        file_pos = find_rightmost_file(disk)

        if space_pos == -1 or file_pos == -1 or file_pos < space_pos:
            break

        disk[space_pos] = disk[file_pos]
        disk[file_pos] = '.'


def calculate_checksum(disk):
    checksum = 0
    for pos, file_id in enumerate(disk):
        if file_id != '.':
            checksum += pos * file_id
    return checksum


def part1(disk: list[int | str]) -> int:
    compact_disk(disk)
    # print("Final disk 1:", ''.join(str(x) if x != '.' else '.' for x in disk))
    return calculate_checksum(disk)


def find_free_block(disk, required_length):
    current_length = 0
    for i, val in enumerate(disk):
        if val == '.':
            current_length += 1
            if current_length >= required_length:
                return i - required_length + 1
        else:
            current_length = 0
    return -1


def find_file_position(disk, file_id):
    start = -1
    end = -1
    for i, val in enumerate(disk):
        if val == file_id:
            if start == -1:
                start = i
            end = i
        elif start != -1:
            break
    return start, end


def compact_disk2(disk):
    max_id = max(x for x in disk if x != '.')

    for file_id in range(max_id, -1, -1):
        file_start, file_end = find_file_position(disk, file_id)
        if file_start == -1:
            continue

        file_size = file_end - file_start + 1
        space_pos = find_free_block(disk, file_size)

        if space_pos != -1 and space_pos < file_start:
            file_content = disk[file_start:file_end + 1]
            disk[space_pos:space_pos + file_size] = file_content
            disk[file_start:file_end + 1] = ['.'] * file_size


def part2(disk: list[int | str]) -> int:
    compact_disk2(disk)
    # print("Final disk 2:", ''.join(str(x) if x != '.' else '.' for x in disk))
    return calculate_checksum(disk)


def main():
    input_txt = utils.get_input(9)
    disk_map = [int(c) for c in input_txt]
    file_lengths = disk_map[0::2]
    free_spaces = disk_map[1::2]
    disk = []
    for i, l in enumerate(file_lengths):
        disk.extend([i] * l)
        if i < len(free_spaces):
            disk.extend(['.'] * free_spaces[i])
    print("Initial disk:", ''.join(str(x) if x != '.' else '.' for x in disk))

    disk2 = copy(disk)

    print(f"Part1: {part1(disk)}")
    print(f"Part2: {part2(disk2)}")


if __name__ == "__main__":
    main()
