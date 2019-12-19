#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints, tuple_add
from utils.intcode import Machine
import bisect


def part1(intcode) -> int:
    total_affected = 0
    for y in range(50):
        for x in range(50):
            pos_in = position_in_beam(intcode, x, y)
            total_affected += pos_in
    return total_affected

def part2(intcode) -> int:
    # Use binary search to find first position (x,y) so that square 100x100 fits into beam
    coord_range = list(range(1000000))


def square_fits(intcode, x, y, n=100):
    a = position_in_beam(intcode, x, y)
    b = position_in_beam(intcode, x, y+n-1)
    c = position_in_beam(intcode, x+n-1, y+n-1)
    d = position_in_beam(intcode, x+n-1, y)
    return a and b and c and d

def position_in_beam(intcode, x, y):
    machine = Machine(0, copy.copy(intcode), deque(), 0)
    machine.inputs.append(x)
    machine.inputs.append(y)
    return bool(machine.run()[-1][0])


# From https://www.geeksforgeeks.org/python-program-for-binary-search/
# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns -1
def binarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r - l)/2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1


def main():
    input_txt = get_input(19)
    int_code_list = ints(input_txt)
    code = defaultdict(int, enumerate(int_code_list))
    p1 = part1(code)
    print(f"Part 1: {p1}")


if __name__ == "__main__":
    main()
