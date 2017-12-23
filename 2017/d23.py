#!/usr/bin/env python

from utils import utils
from collections import defaultdict

operations = [op for op in utils.get_input(23).strip().split('\n')]


def part_one() -> None:
    registers = defaultdict(int)
    result = 0

    idx = 0
    while idx < len(operations):
        operation = operations[idx]
        op = operation.split()

        def val(v):
            try:
                return int(v)
            except:
                return registers[v]

        if op[0] == 'set':
            registers[op[1]] = val(op[2])
        elif op[0] == 'sub':
            registers[op[1]] -= val(op[2])
        elif op[0] == 'mul':
            registers[op[1]] *= val(op[2])
            result += 1
        elif op[0] == 'jnz' and val(op[1]) != 0:
            idx += val(op[2])
            continue
        idx += 1

    print('Part 1: ', result)

def part_two():
    # After reading description of reverse-engineered "assembly"
    h = 0
    for b in range(105700, 122700 + 1, 17):
        for factor in range(2, b):
            if b % factor == 0:
                h += 1
                break
    print('Part 2: ', h)



def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
