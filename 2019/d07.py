#!/usr/bin/env python

import copy
import operator
from itertools import permutations
from typing import List, Tuple
from enum import Enum
from collections import deque

from utils import utils


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
        self.out = 0

        self.operation = {
            1: (operator.add, 4),
            2: (operator.mul, 4),
            3: (self.op_input, 2),
            4: (self.op_output, 2),
            5: (self.op_jump_true, 0),
            6: (self.op_jump_false, 0),
            7: (self.op_lt, 4),
            8: (self.op_eq, 4),
            99: (None, None)
        }

    def op_input(self, std_in: int, idx: int, intcode: List[int]):
        intcode[idx] = std_in

    def op_output(self, idx: int, intcode: List[int]):
        self.out = intcode[idx]

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

    def process_opcode(self, intcode: List[int]):
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
            if p1_mode:
                self.op_output(self.pointer + 1, intcode)
            else:
                self.op_output(intcode[self.pointer + 1], intcode)
        # Handle in
        if op == self.op_input:
            if self.inputs:
                self.state = State.READY
                std_in = self.inputs.popleft()
                if p1_mode:
                    self.op_input(std_in, self.pointer + 1, intcode)
                else:
                    self.op_input(std_in, intcode[self.pointer + 1], intcode)
            else:
                self.state = State.WAIT_FOR_INPUT
                return

        # Handle add, mul, lt, eq
        if op_length == 4:
            if p1_mode:
                x = intcode[self.pointer + 1]
            else:
                x = intcode[intcode[self.pointer + 1]]
            if p2_mode:
                y = intcode[self.pointer + 2]
            else:
                y = intcode[intcode[self.pointer + 2]]
            if p3_mode:
                destination = self.pointer + 3
            else:
                destination = intcode[self.pointer + 3]
            new_value = op(x, y)
            intcode[destination] = new_value

        # Handle jumps
        if op_length == 0:
            if p1_mode:
                x = intcode[self.pointer + 1]
            else:
                x = intcode[intcode[self.pointer + 1]]
            if p2_mode:
                idx = intcode[self.pointer + 2]
            else:
                idx = intcode[intcode[self.pointer + 2]]
            op(x, idx)
        self.pointer += op_length
        return

    def run(self) -> Tuple[State, int]:
        while self.state != State.HALT and not (
                self.state == State.WAIT_FOR_INPUT and len(self.inputs) == 0):
            self.process_opcode(self.code)
        return self.state, self.out


class Scheduler:
    def __init__(self, machines, phase_setting):
        self.machines = machines
        self.connections = self.connect()
        for idx, machine in enumerate(self.machines):
            machine.inputs.append(phase_setting[idx])
        self.machines[0].inputs.append(0)

    def connect(self):
        connections = {}
        for idx in range(len(self.machines)):
            if idx == len(self.machines) - 1:
                connections[self.machines[idx]] = self.machines[0]
            else:
                connections[self.machines[idx]] = self.machines[idx + 1]
        return connections

    def run(self):
        cur_machine = self.machines[0]
        next_machine = self.connections[cur_machine]
        state = cur_machine.state
        out = 0
        while state != State.HALT:
            machine_state, output = cur_machine.run()
            if cur_machine == self.machines[-1]:
                state = machine_state
            out = output
            next_machine.inputs.append(output)
            cur_machine = next_machine
            next_machine = self.connections[cur_machine]
        return out


def determine_phase_setting(intcode):
    best_thrust = 0
    possible_phase_settings = list(permutations(range(5, 10)))
    for phase_setting in possible_phase_settings:
        machines = []
        out = 0
        for i, _ in enumerate(phase_setting):
            new_amplifier = Machine(i, copy.copy(intcode), deque(), 0)
            machines.append(new_amplifier)

        scheduler = Scheduler(machines, phase_setting)
        out = scheduler.run()
        if out > best_thrust:
            best_thrust = out
    print(f'Best: {best_thrust}')


def main():
    input_txt = utils.get_input(7)
    intcode = utils.ints(input_txt)
    determine_phase_setting(intcode)


if __name__ == "__main__":
    main()
