#!/usr/bin/env python

from utils import utils
from collections import defaultdict
from collections import deque
import operator
import re


X_BOUNDARY = 20
Y_BOUNDARY = 10

def print_data(positions):
    print()
    print()
    for y in range(-Y_BOUNDARY, Y_BOUNDARY):
        for x in range(-X_BOUNDARY, X_BOUNDARY):
            if (x, y) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print('\n')


def main():
    data = utils.get_input(11)
    data = data.split('\n')[:-1]
    positions = dict()

    pattern = r'^.*([- ]+[0-9]+).*([- ]+[0-9]+).*([- ]+[0-9]+).*([- ]+[0-9]+)>.*$'
    regex = re.compile(pattern)

    for line in data:
        match = regex.match(line)
        if match:
            pos_x = int(match.group(1))
            pos_y = int(match.group(2))
            vel_x = int(match.group(3))
            vel_y = int(match.group(4))
            positions[(pos_x, pos_y)] = (vel_x, vel_y)

    print_data(positions)

    n = 4
    for _ in range(n):
        new_pos = dict()
        for p in positions.keys():
            v_x, v_y = positions[p]
            new_pos[(p[0] - v_x, p[1] - v_y)] = (v_x, v_y)
        positions = new_pos
        print_data(positions)



    print(data)
    #print(positions)

if __name__ == "__main__":
    main()
