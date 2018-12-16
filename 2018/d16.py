#!/usr/bin/env python

from utils import utils
from collections import defaultdict
import re


class Operation:
    def __init__(self, before, op, after):
        self.before = before
        self.op = op
        self.after = after
        self.possible_ops = []


def addr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] + registers[b]
    return registers_new


def addi(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] + b
    return registers_new


def mulr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] * registers[b]
    return registers_new


def muli(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] * b
    return registers_new


def banr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] & registers[b]
    return registers_new


def bani(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] & b
    return registers_new


def borr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] | registers[b]
    return registers_new


def bori(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] | b
    return registers_new


def setr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a]
    return registers_new


def seti(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = a
    return registers_new


def gtir(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(a > registers[b])
    return registers_new


def gtri(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(registers[a] > b)
    return registers_new


def gtrr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(registers[a] > registers[b])
    return registers_new


def eqir(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(a == registers[b])
    return registers_new


def eqri(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(registers[a] == b)
    return registers_new


def eqrr(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = int(registers[a] == registers[b])
    return registers_new


def parse(line):
    return list(map(int, re.findall(r"\d+", line)))


def get_operations_with_x_possibilities(operations, x):
    two_possible = [op for op in operations if len(op.possible_ops) == x]
    return two_possible


def remove_possibilities(operations, op_assignments):
    for op in operations:
        for i, f in enumerate(op.possible_ops):
            if f in op_assignments.values() and not op.op[0] in op_assignments:
                del op.possible_ops[i]


def find_op_codes(operations, op_assignments):
    op_assignments_new = op_assignments.copy()
    while len(op_assignments_new) < 16:
        only_one_possible = get_operations_with_x_possibilities(operations, 1)
        for op in only_one_possible:
            op_assignments_new[op.op[0]] = op.possible_ops[0]
        remove_possibilities(operations, op_assignments_new)
    return op_assignments_new


def main():
    operations = []
    functions = [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    ]
    op_assignments = dict()

    data = utils.get_input(16).split("\n\n\n")
    lines_p1 = data[0].split("\n")

    for i, line in enumerate(lines_p1):
        if "Before" in line:
            op_lines = lines_p1[i : i + 3]

            reg_before = parse(op_lines[0])
            op = parse(op_lines[1])
            reg_after = parse(op_lines[2])

            this_op = Operation(reg_before, op, reg_after)
            operations.append(this_op)

    for op in operations:
        for f in functions:
            if f(op.op[1], op.op[2], op.op[3], op.before) == op.after:
                op.possible_ops.append(f)

    three_and_above = len([op for op in operations if len(op.possible_ops) >= 3])
    print(f"Part 1 {three_and_above}")

    op_assignments = find_op_codes(operations, op_assignments)

    final_registers = [0] * 4
    lines_p2 = data[1].split("\n")
    for line in lines_p2:
        line = line.strip()
        if not line:
            continue
        op, a, b, c = list(map(int, line.split()))
        f = op_assignments[op]
        final_registers = f(a, b, c, final_registers)
    print(f"Part 2: {final_registers[0]}")


if __name__ == "__main__":
    main()
