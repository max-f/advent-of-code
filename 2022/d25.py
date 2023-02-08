#!/usr/bin/env python

from utils import utils

"""
Code for https://adventofcode.com/2022/day/25
"""


def to_snafu(decimal):
    cur = decimal
    snafu = ""
    while True:
        base_d = cur % 5
        if base_d == 0:
            snafu = "0" + snafu
        elif base_d == 1:
            cur -= 1
            snafu = "1" + snafu
        elif base_d == 2:
            cur -= 2
            snafu = "2" + snafu
        elif base_d == 3:
            cur += 2
            snafu = "=" + snafu
        elif base_d == 4:
            cur += 1
            snafu = "-" + snafu
        cur //= 5

        if cur == 0:
            return snafu


def from_snafu(snafu):
    if snafu:
        *a, b = snafu
        return from_snafu(a) * 5 + "=-012".find(b) - 2
    else:
        return 0


def main():
    input_txt = utils.get_input(25)

    print(to_snafu(sum([from_snafu(x) for x in input_txt.split("\n")])))


if __name__ == "__main__":
    main()
