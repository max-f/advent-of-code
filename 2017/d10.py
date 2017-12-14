#!/usr/bin/env python

import functools
import itertools
import operator


def circ_slice(xs: list, start: int, length: int):
    it = itertools.cycle(xs)
    next(itertools.islice(it, start, start), None)
    return list(itertools.islice(it, length))


def part_one(lengths: list, elements: list, idx: int = 0, skip_size: int = 0) -> tuple:
    for length in lengths:
        if length > len(elements):
            continue
        affected_elements = circ_slice(elements, idx, length)

        orig_idcs = [elements.index(e) for e in affected_elements]
        reversed_idcs = orig_idcs[::-1]
        for i in range(len(orig_idcs) // 2):
            orig_idx = orig_idcs[i]
            reversed_idx = reversed_idcs[i]
            tmp = elements[reversed_idx]
            elements[reversed_idx] = elements[orig_idx]
            elements[orig_idx] = tmp

        idx += (length + skip_size) % len(elements)
        skip_size += 1
    return elements, idx, skip_size


def create_hash(input_str: str) -> str:
    ascii_lengths = list(map(ord, input_str)) + [17, 31, 73, 47, 23]

    idx = 0
    skip_size = 0
    elements = list(range(256))

    for round in range(64):
        elements, idx, skip_size = part_one(ascii_lengths, elements, idx, skip_size)

    dense_hash = []
    for idx in range(0, len(elements), 16):
        dense_element = functools.reduce(operator.xor, (elements[idx:idx + 16]))
        dense_hash.append(dense_element)

    print(dense_hash)
    hexa_str = ''
    for dense_number in dense_hash:
        hexa_str += f'{dense_number:02x}'
    return hexa_str


def main():
    lengths_str = '88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205'

    lengths = list(map(int, lengths_str.split(',')))
    elements, idx, skip_size = part_one(lengths, list(range(256)))
    print(elements[0] * elements[1])

    hash = create_hash(lengths_str)
    print(hash)


if __name__ == '__main__':
    main()
