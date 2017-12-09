#!/usr/bin/env python

from utils import utils


def parse(day: int) -> None:
    score = 0
    open_groups = 0
    is_garbage = False
    is_canceled = False
    garbage_count = 0

    input_str = utils.get_input(day)
    test_str1 = '{{<a!>},{<a!>},{<a!>},{<ab>}}'  # score: 3
    test_str2 = '{{<!!>},{<!!>},{<!!>},{<!!>}}'  # score: 9
    test_str3 = '{{<ab>},{<ab>},{<ab>},{<ab>}}'  # score: 9
    for char in input_str:
        # for char in test_str3:
        if is_canceled:
            is_canceled = False
            continue
        if not is_canceled and char == '!':
            is_canceled = True
            continue
        elif is_garbage and char == '>':
            is_garbage = False
        elif is_garbage:
            is_canceled = False
            garbage_count += 1
            continue
        elif char == '<':
            is_garbage = True
        elif char == '{':
            open_groups += 1
        elif open_groups and char == '}':
            score += open_groups
            open_groups -= 1

        is_canceled = False
    # assert score == 9
    print(score)
    print(garbage_count)


def main():
    parse(9)


if __name__ == '__main__':
    main()
