#!/usr/bin/env python

from collections import Counter
from collections import defaultdict

def part_one():
    tapes = defaultdict(int)
    state = 0
    idx = 0
    for _ in range(12261543):
        if state == 0:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 1
            else:
                tapes[idx] = 0
                idx -= 1
                state = 2
        elif state == 1:
            if not tapes[idx]:
                tapes[idx] = 1
                idx -= 1
                state = 0
            else:
                tapes[idx] = 0
                idx += 1
                state = 2
        elif state == 2:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 0
            else:
                tapes[idx] = 0
                idx -= 1
                state = 3
        elif state == 3:
            if not tapes[idx]:
                tapes[idx] = 1
                idx -= 1
                state = 4
            else:
                tapes[idx] = 1
                idx -= 1
                state = 2
        elif state == 4:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 5
            else:
                tapes[idx] = 1
                idx += 1
                state = 3
        elif state == 5:
            if not tapes[idx]:
                tapes[idx] = 1
                idx += 1
                state = 0
            else:
                tapes[idx] = 1
                idx += 1
                state = 4

    print(tapes)
    result_list = [v for v in tapes.values()]
    print(result_list)
    print(sum(result_list))


def main():
    part_one()


if __name__ == '__main__':
    main()
