#!/usr/bin/env python

from utils import utils


def calc_sum_p1(input_txt: str) -> int:
    overall = 0
    lines = input_txt.split("\n")
    for x in lines:
        x = x.rstrip("\n")
        if x:
            overall += int(x)
    return overall


def calc_recurring_freq(input_txt: str) -> int:
    freq = 0
    reached_freq = set()
    reached_freq.add(0)
    lines = input_txt.split("\n")
    while True:
        for x in lines:
            x = x.rstrip("\n")
            if x:
                freq += int(x)
                if freq in reached_freq:
                    return freq
                else:
                    reached_freq.add(freq)


def main():
    input_txt = utils.get_input(1)
    input_sum_one = calc_sum_p1(input_txt)
    cycle = calc_recurring_freq(input_txt)
    print(f"Part 1: {input_sum_one}")
    print(f"Part 2: {cycle}")


if __name__ == "__main__":
    main()
