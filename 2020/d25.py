#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2020/day/25
"""


def calculate(subject_nr: int, pk=None, loop_nr: int = 10000000) -> tuple[int, bool]:
    value = 1
    for loop_nr in range(1, loop_nr):
        value *= subject_nr
        value %= 20201227
        if pk and value == pk:
            return loop_nr, True
    return value, False


def main():
    input_txt = utils.get_input(25).rstrip()
    card_subj = 7
    # door_subj = 11
    card_pk, door_pk = (int(x) for x in input_txt.split("\n"))

    loop_card, reverse = calculate(card_subj, card_pk)
    # loop_door, reverse = calculate(door_subj, door_pk)
    print(f"Card {loop_card} - {reverse}")
    # print(f'Door {loop_door} - {reverse}')

    if reverse and loop_card > 0:
        print(f"Encryption key: {calculate(door_pk, loop_nr=loop_card + 1)[0]}")


if __name__ == "__main__":
    main()
