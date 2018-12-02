#!/usr/bin/env python

from collections import defaultdict
from utils import utils


def get_occurences(line):
    occs = defaultdict(int)
    line = line.strip()
    for c in line:
        occs[c] += 1
    return occs


def compare(str1, str2):
    one_time = False
    idx = 0
    for i, x in enumerate(str1):
        if len(str1) == len(str2) and x != str2[i] and not one_time:
            one_time = True
            idx = i
        elif len(str1) == len(str2) and x != str2[i] and one_time:
            one_time = False
            break
    return (one_time, idx)


def main():
    input_txt = utils.get_input(2)
    lines = input_txt.split("\n")
    twos = 0
    threes = 0
    for line in lines:
        f1 = False
        f2 = False
        occs = get_occurences(line)
        for occ in occs.values():
            if occ == 2 and not f1:
                twos += 1
                f1 = True
            elif occ == 3 and not f2:
                threes += 1
                f2 = True
    p1 = threes * twos
    print(f"Part 1: {p1}")

    for i, line_a in enumerate(lines):
        for line_b in lines[i + 1 :]:
            one_time, idx = compare(line_a, line_b)
            if one_time:
                solution = list(line_a)
                del solution[idx]
                print(f"Part 2: {''.join(solution)}")
                return


if __name__ == "__main__":
    main()
