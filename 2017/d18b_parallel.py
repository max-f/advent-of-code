#!/usr/bin/env python

from utils import utils
from collections import defaultdict
import multiprocessing as mp
import multiprocessing.pool


operations = [op for op in utils.get_input(18).split('\n')]


def run_program(identity: int, inqueue, outqueue) -> int:
    registers = defaultdict(int)
    registers['p'] = identity

    def val(v):
        try:
            return int(v)
        except:
            return registers[v]

    idx = 0
    result = 0
    while 0 <= idx < len(operations) - 1:
        op = operations[idx].split()

        if op[0] == 'set':
            registers[op[1]] = val(op[2])
        elif op[0] == 'add':
            registers[op[1]] += val(op[2])
        elif op[0] == 'mul':
            registers[op[1]] *= val(op[2])
        elif op[0] == 'mod':
            registers[op[1]] %= val(op[2])
        elif op[0] == 'snd':
            if outqueue:
                outqueue.put(val(op[1]))
            result += 1
        elif op[0] == 'rcv':
            if inqueue:
                try:
                    registers[op[1]] = inqueue.get(timeout=1)
                except:
                    return result
        elif op[0] == 'jgz' and val(op[1]) > 0:
            idx += val(op[2])
            continue
        idx += 1


def part_two():
    pool = multiprocessing.pool.ThreadPool(processes=2)

    q1 = mp.Queue()
    q2 = mp.Queue()

    result1 = pool.apply_async(run_program, (0, q1, q2))
    result2 = pool.apply_async(run_program, (1, q2, q1))

    result1.get()
    print('Part two: ', result2.get())


def main():
    part_two()

if __name__ == '__main__':
    main()
