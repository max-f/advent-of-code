#!/usr/bin/env python

import operator
import re

from utils import utils

ops = {'inc': operator.add,
       'dec': operator.sub,
       '<':   operator.lt,
       '<=':  operator.le,
       '>':   operator.gt,
       '>=':  operator.ge,
       '==':  operator.eq,
       '!=':  operator.ne
       }

registers = {}


def execute_instructions(day: int) -> None:
    # cy inc -232 if scy > -8
    pattern = r'(\w+) (\w+) (-*\d+) \w+ (\w+) ([>=<!]+) (-*\d+).*'
    regex = re.compile(pattern)
    max_value = 0

    input_str = utils.get_input(day)
    for line in input_str.split('\n'):
        match = regex.match(line)
        if match:
            mod_register = match.group(1)
            mod_op = match.group(2)
            mod_value = int(match.group(3))
            check_register = match.group(4)
            bool_op = match.group(5)
            check_value = int(match.group(6))

            check_current_val = registers.get(check_register, 0)

            if ops[bool_op](check_current_val, check_value):
                mod_current_val = registers.get(mod_register, 0)
                registers[mod_register] = ops[mod_op](mod_current_val, mod_value)
                if registers[mod_register] > max_value:
                    max_value = registers[mod_register]

    print('Part 1: ', max(registers.values()))
    print('Part 2: ', max_value)


def main():
    execute_instructions(8)


if __name__ == '__main__':
    main()
