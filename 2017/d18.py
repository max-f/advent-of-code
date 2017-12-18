#!/usr/bin/env python

from utils import utils
from collections import defaultdict

operations = [op for op in utils.get_input(18).split('\n')]


def part_one() -> None:
    registers = defaultdict(int)
    last_sound = 0

    idx = 0
    while True:
        operation = operations[idx]
        op = operation.split()

        val1 = None
        if not op[1].islower():
            val1 = int(op[1])

        val2 = None
        if len(op) == 3:
            try:
                val2 = int(op[2])
            except ValueError:
                val2 = registers[op[2]]

        if op[0] == 'set':
            registers[op[1]] = val2
        elif op[0] == 'add':
            registers[op[1]] += val2
        elif op[0] == 'mul':
            registers[op[1]] *= val2
        elif op[0] == 'mod':
            registers[op[1]] %= val2
        elif op[0] == 'snd':
            last_sound = registers[op[1]]
        elif op[0] == 'rcv' and last_sound != 0:
            break
        elif op[0] == 'jgz':
            if val1 or registers[op[1]] != 0:
                idx += val2
                continue
        idx += 1

    print('Part 1: ', last_sound)


def run_program(identity: int, idx: int, registers: dict):
    other_id = 1 - identity

    def val(v):
        try:
            return int(v)
        except:
            return registers[v]

    while True:
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
            queues[other_id].append(val(op[1]))
            if identity == 1:
                global result
                result += 1
        elif op[0] == 'rcv':
            if queues[identity]:
                registers[op[1]] = queues[identity].pop(0)
                states[identity] = 'ok'
            else:
                if states[other_id] == 'done':
                    states[identity] = 'done'
                    return idx, registers
                if states[other_id] == 'r' and not queues[other_id]:
                    states[identity] = 'done'
                    return idx, registers
                states[identity] = 'r'
                return idx, registers

        elif op[0] == 'jgz' and val(op[1]) > 0:
            idx += val(op[2])
            continue
        idx += 1
        if idx >= len(operations):
            states[identity] = 'done'
            return idx, registers


def part_two():
    global queues
    queues = {
        0: list(),
        1: list()
    }
    global states
    states = ['ok', 'ok']
    global result
    result = 0

    registers_one = defaultdict(int)
    registers_one['p'] = 0
    registers_two = defaultdict(int)
    registers_two['p'] = 1
    idx_one = 0
    idx_two = 0

    i = 0
    while not all([state == 'done' for state in states]):
        idx_one, registers_one = run_program(0, idx_one, registers_one)
        idx_two, registers_two = run_program(1, idx_two, registers_two)
        i += 1
    print('Part 2: ', result)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
