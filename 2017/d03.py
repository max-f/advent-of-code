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

def part_two(num: int) -> int:
    size = 0
    x = 0
    y = 0
    dx, dy = 1, 0

    sums = {(0, 0): 1}

    while True:
        if max(abs(x + dx), abs(y + dy)) > size:
            if x == size and y == -size:
                size += 1
            else:
                dx, dy = left_turn(dx, dy)
            
        x += dx
        y += dy

        sum = 0
        sum += calculate_neighbor_sum(x, y, sums)
        sums[(x, y)] = sum
        if sum >= num:
            print(sum)
            break


def left_turn(dx: int, dy: int) -> tuple:
    if (dx, dy) == (1, 0):
        return (0, 1)
    elif (dx, dy) == (0, 1):
        return (-1, 0)
    elif (dx, dy) == (-1, 0):
        return (0, -1)
    else:
        return (1, 0)


def calculate_neighbor_sum(x: int, y: int, sums: dict) -> int:
    sum = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            sum += sums.get((x + i, y + j), 0)  # add nothing if element not set (yet)
    return sum


def main():
    part_one(361527)
    part_two(361527)


if __name__ == '__main__':
    main()
