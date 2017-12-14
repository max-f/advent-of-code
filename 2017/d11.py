#!/usr/bin/env python

from utils import utils


# After consulting https://www.redblobgames.com/grids/hexagons/ :E

def walk(day: int) -> None:
    x = 0
    y = 0
    z = 0

    input_str = utils.get_input(11)
    # input_str = 'ne,ne,ne'
    # input_str = 'ne,ne,sw,sw'
    # input_str = 'ne,ne,s,s'
    # input_str = 'se,sw,se,sw,sw'

    distances = []
    for d in input_str.rstrip().split(','):
        if d == 'n':
            y += 1
            z -= 1
        elif d == 'ne':
            x += 1
            z -= 1
        elif d == 'se':
            x += 1
            y -= 1
        elif d == 's':
            y -= 1
            z += 1
        elif d == 'sw':
            x -= 1
            z += 1
        elif d == 'nw':
            x -= 1
            y += 1
        distances.append((abs(x) + abs(y) + abs(z)) // 2)
    print((abs(x) + abs(y) + abs(z)) // 2)
    print(max(distances))


def main():
    walk(11)


if __name__ == '__main__':
    main()
