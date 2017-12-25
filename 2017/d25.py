#!/usr/bin/env python

from collections import defaultdict


def part_one():
    tapes = defaultdict(int)
    state = 0
    idx = 0
    for _ in range(12261543):
        # A
        if state == 0:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 1
            else:
                tapes[idx] = 0
                idx -= 1
                state = 2
        # B
        elif state == 1:
            if not tapes[idx]:
                tapes[idx] = 1
                idx -= 1
                state = 0
            else:
                tapes[idx] = 1
                idx += 1
                state = 2
        # C
        elif state == 2:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 0
            else:
                tapes[idx] = 0
                idx -= 1
                state = 3
        # D
        elif state == 3:
            if not tapes[idx]:
                tapes[idx] = 1
                idx -= 1
                state = 4
            else:
                tapes[idx] = 1
                idx -= 1
                state = 2
        # E
        elif state == 4:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 5
            else:
                tapes[idx] = 1
                idx += 1
                state = 0
        # F
        elif state == 5:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 0
            else:
                tapes[idx] = 1
                idx += 1
                state = 4

    result_list = [v for v in tapes.values()]
    print(sum(result_list))


def main():
    part_one()


if __name__ == '__main__':
    main()
