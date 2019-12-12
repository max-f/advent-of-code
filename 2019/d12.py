#!/usr/bin/env python

import copy
from collections import deque, defaultdict

from enum import Enum
from utils.utils import get_input, ints
from utils.intcode import Machine, State


def main():
    input_txt = get_input(12)
    int_code_list = ints(input_txt)
    code = defaultdict(int, enumerate(int_code_list))


if __name__ == "__main__":
    main()
