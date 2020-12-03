#!/usr/bin/env python

import operator
from collections import deque
from enum import Enum
from typing import Tuple, Dict, List


class State(Enum):
    READY = 0
    WAIT_FOR_INPUT = 1
    HALT = 2


class Machine:
    def __init__(self, idx, code, inputs: deque, pointer):
        self.idx = idx
        self.state = State.READY
        self.code = code
        self.inputs = inputs
        self.pointer = pointer
        self.relative_base = 0
        self.out = []

        self.operation = {
            1: (operator.add, 4),
            2: (operator.mul, 4),
            3: (self.op_input, 2),
            4: (self.op_output, 2),
            5: (self.op_jump_true, 0),
            6: (self.op_jump_false, 0),
            7: (self.op_lt, 4),
            8: (self.op_eq, 4),
            9: (self.op_relative_base_offset, 2),
            99: (None, None)
        }

    def op_relative_base_offset(self, relative_base: int):
        self.relative_base += relative_base

    def op_input(self, std_in: int, idx: int, intcode: Dict[int, int]):
        pass

    def op_output(self, value: int):
        # print(f'Output: {value}')
        self.out.append(value)

    def op_jump_true(self, x: int, idx: int):
        if x != 0:
            self.pointer = idx
        else:
            self.pointer += 3

    def op_jump_false(self, x: int, idx: int):
        if x == 0:
            self.pointer = idx
        else:
            self.pointer += 3

    def op_lt(self, x: int, y: int) -> int:
        if x < y:
            return 1
        return 0

    def op_eq(self, x: int, y: int) -> int:
        if x == y:
            return 1
        return 0

    def read(self, mode, param) -> int:
        idx = -1
        # Positional mode
        if mode == 0:
            idx = self.code[self.pointer + param]
        # Immediate mode
        elif mode == 1:
            idx = self.pointer + param
        # Relative mode
        elif mode == 2:
            idx = self.relative_base + self.code[self.pointer + param]
        # Unsupported mode
        else:
            raise Exception(f"Unknown mode {mode} for writing parameter {idx}")
        return self.code[idx]

    def write(self, mode, param, value) -> None:
        idx = -1
        # Positional mode
        if mode == 0:
            idx = self.code[self.pointer + param]
        # Relative mode
        elif mode == 2:
            idx = self.relative_base + self.code[self.pointer + param]
        # Unsupported mode
        else:
            raise Exception(f"Unknown mode {mode} for writing parameter {idx}")
        self.code[idx] = value

    def process_opcode(self, intcode: Dict[int, int]):
        modes_and_opcode = [
            int(x) for x in str(intcode[self.pointer]).zfill(5)
        ]
        p1_mode = modes_and_opcode[2]
        p2_mode = modes_and_opcode[1]
        p3_mode = modes_and_opcode[0]
        opcode = int("".join(map(str, modes_and_opcode[-2:])))

        op, op_length = self.operation[opcode]
        if not op:
            self.state = State.HALT
            return

        # Handle out
        if op == self.op_output:
            out_value = self.read(p1_mode, 1)
            self.op_output(out_value)

        # Handle relative base op
        if op == self.op_relative_base_offset:
            relative_base_value = self.read(p1_mode, 1)
            self.op_relative_base_offset(relative_base_value)

        # Handle in
        if op == self.op_input:
            if self.inputs:
                self.state = State.READY
                std_in = self.inputs.popleft()
                self.write(p1_mode, 1, std_in)
            else:
                self.state = State.WAIT_FOR_INPUT
                return

        # Handle add, mul, lt, eq
        if op_length == 4:
            x = self.read(p1_mode, 1)
            y = self.read(p2_mode, 2)
            new_value = op(x, y)
            self.write(p3_mode, 3, new_value)

        # Handle jumps
        if op_length == 0:
            x = self.read(p1_mode, 1)
            idx = self.read(p2_mode, 2)
            op(x, idx)

        self.pointer += op_length
        return

    def run(self) -> Tuple[State, List[int]]:
        while self.state != State.HALT and not (
                self.state == State.WAIT_FOR_INPUT and len(self.inputs) == 0):
            self.process_opcode(self.code)
        return self.state, self.out
