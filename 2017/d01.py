#!/usr/bin/env python

from typing import List, Callable

from utils import utils


def find_halfway_matching_pairs(xs: list) -> list:
    matching_pair_elements = list()
    matched_already = [False] * len(xs)
    for i, x in enumerate(xs):
        if matched_already[i]:
            continue
        find_idx = int((i + len(xs) / 2) % len(xs))
        if x == xs[find_idx]:
            matching_pair_elements.append(x)
            matched_already[i] = True

    return matching_pair_elements


def find_direct_matching_pairs(xs: list) -> list:
    xs_extended = list(xs)
    xs_extended.append(xs[0])
    tuple_list = list(zip(xs, xs_extended[1::]))
    matching_pair_elements = [t[0] for t in tuple_list if len(set(t)) == 1]
    return matching_pair_elements


def calc_sum(input_txt: str, fun: Callable[[List[int]], list]) -> int:
    xs = [int(i) for i in input_txt.rstrip()]
    elements_to_sum = fun(xs)
    return sum(elements_to_sum)


def main():
    test = '12131415'
    test_sum = calc_sum(test, find_halfway_matching_pairs)
    assert test_sum == 4
    input_txt = utils.get_input(1)
    input_sum_one = calc_sum(input_txt, find_direct_matching_pairs)
    input_sum_two = calc_sum(input_txt, find_halfway_matching_pairs)
    print('Sum Part 1: {}'.format(input_sum_one))
    print('Sum Part 2: {}'.format(input_sum_two))


if __name__ == '__main__':
    main()
