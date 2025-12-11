#!/usr/bin/env python

from functools import cache

from utils import utils

"""
Code for https://adventofcode.com/2025/day/11
"""

edges = {}


@cache
def paths_from(node, dac: bool = True, fft: bool = True):
    match node:
        case "out":
            return dac and fft
        case "dac":
            dac = True
        case "fft":
            fft = True
    return sum(paths_from(v, dac, fft) for v in edges[node])


def main():
    input_txt = utils.get_input(11)
    lines = input_txt.strip().splitlines()

    global edges
    for line in lines:
        words = utils.words(line)
        edges[words[0]] = words[1:]

    print(f"Part1: {paths_from('you')}")
    print(f"Part2: {paths_from('svr', False, False)}")


if __name__ == "__main__":
    main()
