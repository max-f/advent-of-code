#!/usr/bin/env python

from d10 import create_hash

def create_grid(input_str: str) -> None:
    grid = []
    result = 0
    for i in range(128):
        line = input_str + '-' + str(i)
        hash = create_hash(line)
        if hash:
            scale = 16 # equals to hexadecimal
            num_of_bits = 128
            binary_number = bin(int(hash, scale))[2:].zfill(num_of_bits)
            grid.append(binary_number)
            result += binary_number.count('1')
    # Part 1
    print(result)


    used_positions = []
    for i, line in enumerate(grid):
        row = [(i, j) for j, c in enumerate(line) if int(c)]
        used_positions.extend(row)

    groups = 0
    while used_positions:
        to_bre_removed = [used_positions[0]]
        while to_bre_removed:
            (x, y) = to_bre_removed.pop()
            if (x, y) in used_positions:
                used_positions.remove((x, y))
                to_bre_removed.extend([(x-1, y), (x, y-1), (x+1, y), (x, y+1)])
        groups += 1
    print(groups)


def main():
    input_str = 'ffayrhll'
    create_grid(input_str)


if __name__ == '__main__':
    main()
