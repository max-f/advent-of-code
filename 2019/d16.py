#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from utils.utils import get_input, ints, tuple_add
import re
import networkx as nx
from fractions import Fraction
import math
from pprint import pprint


def part1(number_list, times=100):
    base_pattern = [0, 1, 0, -1]
    for _ in range(times):
        for idx, _ in enumerate(number_list):
            new_elem = 0
            # numbers before current idx won't matter for the sum as they will zero out
            for i, elem in enumerate(number_list[idx:], idx):
                # idx is the number of repeats in the base pattern
                pattern_coefficient = base_pattern[((i + 1) // (idx + 1)) % len(base_pattern)]
                new_elem += elem * pattern_coefficient
            # Can assign already to number_list since we only look at later digits for coming iterations
            number_list[idx] = int(str(new_elem)[-1])
    print(''.join(map(str, number_list[:8])))


def main():
    input_txt = get_input(16)
    number_list = list(map(int, list(input_txt)))
    part1(number_list)


if __name__ == "__main__":
    main()
