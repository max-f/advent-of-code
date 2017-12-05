#!/usr/bin/env python

def part_one(x: int):
    i = 1
    while ((i + 2) ** 2) < x:
        i += 2
    pos_last_spiral = (x - (i ** 2)) - 1
    distances = build_ith_spiral(i + 2)
    print(distances[pos_last_spiral])


def build_ith_spiral(i: int) -> list:
    distances = [0] * i
    distances[0] = 2 * (i // 2)
    for x in range(1, i // 2 + 1):
        distances[x] = distances[x - 1] - 1
    for x in range(i // 2 + 1, 2 * (i // 2) + 1):
        distances[x] = distances[x - 1] + 1
    distances.extend(distances[1:])
    distances.extend(distances[1:])
    distances = distances[1:]
    return distances


def main():
    part_one(361527)


if __name__ == '__main__':
    main()
