#!/usr/bin/env python

from collections import deque
from itertools import product

from utils import utils

num_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

robot_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


def compute_sequences(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)

    seqs = {}
    for start in pos:
        for end in pos:
            if start == end:
                seqs[(start, end)] = ['A']
                continue

            possibilities = []
            q = deque([(pos[start], "")])
            shortest = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == end:
                        if shortest < len(moves) + 1: break
                        shortest = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break

            seqs[(start, end)] = possibilities
    return seqs


num_seqs = compute_sequences(num_keypad)

robot_seqs = compute_sequences(robot_keypad)
robot_seq_lengths = {k: len(v[0]) for k, v in robot_seqs.items()}


def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]


def find_shortest_string(nested_list):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            elif isinstance(item, str):
                result.append(item)
        return result

    flat_strings = flatten(nested_list)

    if not flat_strings:
        return None

    return min(flat_strings, key=len)

def part1(codes):
    total = 0
    for code in codes:
        numeric_part = int(code[:-1])

        first_enc = solve(code, num_seqs)
        second_enc = [solve(enc, robot_seqs) for enc in first_enc]
        third_enc = [[solve(enc, robot_seqs) for enc in xs] for xs in second_enc]

        # print(third_enc)
        minimal_encoding = find_shortest_string(third_enc)
        print(len(minimal_encoding))

        complexity = len(minimal_encoding) * numeric_part
        total += complexity
    return total


def main() -> None:
    input_txt = utils.get_input(21)
    codes = input_txt.strip().split("\n")

    print(f"Part1: {part1(codes)}")
    # print(f"Part2: {part2(grid, G, start, end)}")


if __name__ == "__main__":
    main()
