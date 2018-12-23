#!/usr/bin/env python

from utils import utils


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
    a = sum([ord(x) for x in str(a)])
    b = sum([ord(x) for x in str(b)])
    registers_new[c] = registers[a] & registers[b]
    return registers_new


def bani(a, b, c, registers):
    registers_new = registers.copy()
    registers_new[c] = registers[a] & b
    return registers_new


def borr(a, b, c, registers):
    registers_new = registers.copy()
    a = sum([ord(x) for x in str(a)])
    b = sum([ord(x) for x in str(b)])
    registers_new[c] = registers[a] | registers[b]
    return registers_new


def bori(a, b, c, registers):
    registers_new = registers.copy()
    a = sum([ord(x) for x in str(a)])
    b = sum([ord(x) for x in str(b)])
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


def main():
    functions = {
        'addr': addr,
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtir': gtir,
        'gtri': gtri,
        'gtrr': gtrr,
        'eqir': eqir,
        'eqri': eqri,
        'eqrr': eqrr,
    }

    lines = utils.get_input(21).split("\n")
    # Read in instruction pointer binding
    ip = int(lines[0].split()[-1])

    # Read in operations
    operations = [None] * (len(lines) - 1)
    for i, line in enumerate(lines[1:]):
        if line:
            op, a, b, c = line.split()
            operations[i] = (op, int(a), int(b), int(c))

    print(operations)
    print(len(operations))

    # Set initial register values
    # Part 1
    # registers = [0] * 6
    # Part 2
    minimal = 0
    for x in range(10000):
        registers = [x, 0, 0, 0, 0, 0]
        iterations = 0

        while iterations < 500:
            if registers[ip] < 0 or registers[ip] > len(operations):
                minimal = x
                print(minimal)
                return
            #print('before', registers, end='  ')
            next_op, a, b, c = operations[registers[ip]]
            registers = functions[next_op](a, b, c, registers)

            # Default increment instruction pointer by 1
            registers[ip] += 1
            #print('after', registers)
            iterations += 1

    print(registers[0])


if __name__ == "__main__":
    main()
