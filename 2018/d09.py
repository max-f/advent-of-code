#!/usr/bin/env python

from utils import utils
from collections import defaultdict
from collections import deque
import operator

SPECIAL_MARBLE_23 = 23


def get_normal_idx(idx, length):
    idx += 2
    if idx > length:
        return idx - length
    return idx


def get_counter_clockwise_idx(idx, length):
    idx -= 7
    if idx < 0:
        return idx + length
    return idx


def part_1(players, last_marble_points):
    player_scores = defaultdict(int)
    marbles = [0]
    marble_points = 1
    idx = 0

    while True:
        for p in range(1, players + 1):

            if marble_points % SPECIAL_MARBLE_23 != 0:
                idx = get_normal_idx(idx, len(marbles))
                marbles.insert(idx, marble_points)

            else:
                player_scores[p] += marble_points
                idx = get_counter_clockwise_idx(idx, len(marbles))
                marble = marbles.pop(idx)
                player_scores[p] += marble

            marble_points += 1

            if marble_points > last_marble_points:
                print(max(player_scores.items(), key=operator.itemgetter(1))[0])
                return max(player_scores.items(), key=operator.itemgetter(1))[1]


def part_2(players, last_marble_points):
    player_scores = defaultdict(int)
    marbles = deque()
    marbles.append(0)

    for marble_points in range(1, last_marble_points + 1):

        current_player = marble_points % players

        if marble_points % SPECIAL_MARBLE_23 != 0:
            marbles.rotate(-1)
            marbles.append(marble_points)

        else:
            marbles.rotate(7)
            marble_7_counter_clockwise = marbles.pop()
            player_scores[current_player] += marble_points + marble_7_counter_clockwise
            marbles.rotate(-1)

    print(max(player_scores.items(), key=operator.itemgetter(1))[0])
    return max(player_scores.items(), key=operator.itemgetter(1))[1]


def main():
    data = utils.get_input(9)
    data = data.split()
    players = int(data[0])
    last_marble_points = int(data[-2])

    # Test case, part 1: 32
    # players = 9
    # last_marble_points = 25

    # Test case, part 1: 8317
    # players = 10
    # last_marble_points = 1618

    # Could be both done with part_2 method in a more optimal way but
    # leaving part_1 as I got the solution this way.

    print(f"Part 1: {part_1(players, last_marble_points)}")

    print(f"Part 2: {part_2(players, last_marble_points * 100)}")


if __name__ == "__main__":
    main()
