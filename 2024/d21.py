#!/usr/bin/env python

from collections import deque
from itertools import product
import functools

from utils import utils

DIRECTIONS = [((-1, 0), "^"), ((1, 0), "v"), ((0, -1), "<"), ((0, 1), ">")]

NUM_KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

ROBOT_KEYPAD = [
    [None, "^", "A"],
    ["<", "v", ">"],
]


def compute_sequences(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r, c)

    seqs = {}
    for start in pos:
        for end in pos:
            if start == end:
                seqs[(start, end)] = ["A"]
                continue

            possibilities = []
            q = deque([(pos[start], "")])
            shortest = float("inf")
            while q:
                (r, c), moves = q.popleft()

                for (dr, dc), nm in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]):
                        continue
                    if keypad[nr][nc] is None:
                        continue
                    if keypad[nr][nc] == end:
                        if shortest < len(moves) + 1:
                            break
                        shortest = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break

            seqs[(start, end)] = possibilities
    return seqs


def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]


def part1(codes):
    total = 0
    for code in codes:
        numeric_part = int(code[:-1])
        inputs = solve(code, num_seqs)
        length = min(calc_length(code, depth=2) for code in inputs)
        total += length * numeric_part
    return total


@functools.cache
def calc_length(code, depth=25):
    if depth == 1:
        return sum(
            robot_seq_lengths[(start, end)] for start, end in zip("A" + code, code)
        )
    length = 0
    for start, end in zip("A" + code, code):
        length += min(
            calc_length(subseq, depth - 1) for subseq in robot_seqs[(start, end)]
        )
    return length


def part2(codes):
    total = 0
    for code in codes:
        inputs = solve(code, num_seqs)
        length = min(map(calc_length, inputs))
        total += length * int(code[:-1])
    return total


def main() -> None:
    input_txt = utils.get_input(21)
    codes = input_txt.strip().split("\n")

    global num_seqs, robot_seqs, robot_seq_lengths
    num_seqs = compute_sequences(NUM_KEYPAD)
    robot_seqs = compute_sequences(ROBOT_KEYPAD)
    robot_seq_lengths = {k: len(v[0]) for k, v in robot_seqs.items()}

    print(f"Part1: {part1(codes)}")
    print(f"Part2: {part2(codes)}")


if __name__ == "__main__":
    main()
