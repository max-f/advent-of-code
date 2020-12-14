#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/14
"""


def part1(lines: list[str]) -> int:
    bitmask = ''
    memory = {}
    for line in lines:
        cmd, arg = line.split(' = ')
        if cmd == 'mask':
            bitmask = arg
            continue

        mem_idx, value = cmd[4:-1], int(arg)
        value_binary = format(value, '036b')
        combined_binary = [x if bitmask[i] == 'X' else bitmask[i] for i, x in enumerate(value_binary)]
        memory[mem_idx] = ''.join(combined_binary)

    return sum(int(binary_str, 2) for binary_str in memory.values())


def part2(lines: list[str]) -> int:
    bitmask = ''
    memory = {}
    for line in lines:
        cmd, arg = line.split(' = ')
        if cmd == 'mask':
            bitmask = arg
            continue

        mem_idx, value = int(cmd[4:-1]), int(arg)
        mem_idx_bin = format(mem_idx, '036b')
        for mem_idx in calculate_all_memory_addresses(bitmask, mem_idx_bin):
            memory[mem_idx] = value
        memory[mem_idx] = value

    return sum(memory.values())


def calculate_all_memory_addresses(bitmask: str, mem_idx_bin: str) -> list[str]:
    memory_addresses = []
    empty = []
    memory_addresses.append(empty)
    for i, c in enumerate(bitmask):
        new_variants = []
        if c == '0':
            for b_str in memory_addresses:
                b_str.append(mem_idx_bin[i])
        elif c == '1':
            for b_str in memory_addresses:
                b_str.append('1')
        else:
            for b_str in memory_addresses:
                copied_str = b_str.copy()
                b_str.append('0')
                copied_str.append('1')
                new_variants.append(copied_str)
        if new_variants:
            memory_addresses.extend(new_variants)
    return [''.join(binary_c_list) for binary_c_list in memory_addresses]


def main():
    input_txt = utils.get_input(14).rstrip()
    lines = input_txt.split('\n')
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
