#!/usr/bin/env python

from utils import utils
from functools import cmp_to_key
from collections import Counter

"""
Code for https://adventofcode.com/2023/day/7
"""

rank_order = {rank: i for i, rank in enumerate("J23456789TQKA")}
rank_order2 = {rank: i for i, rank in enumerate("23456789TJQKA")}


def hand_rank(hand, p2=False):
    global rank_order, rank_order2
    if p2:
        card_ranking = rank_order
    else:
        card_ranking = rank_order2
    ranked_hand = [card_ranking[card] for card in hand]
    counter = Counter(ranked_hand)

    if p2:
        joker_count = counter.pop(card_ranking["J"], 0)

        # If the counter is empty after popping the Joker cards, return a default hand rank
        if not counter:
            return 9, ranked_hand  # five J's

        # Find the card that appears most frequently in the hand
        most_common_card, _ = counter.most_common(1)[0]

        # Add the number of Joker cards to the most common card
        counter[most_common_card] += joker_count

    # Count the frequency of each card in the hand
    counts = sorted(counter.values(), reverse=True)

    if counts == [5]:
        return 9, ranked_hand  # five of a kind
    elif counts == [4, 1]:
        return 8, ranked_hand  # four of a kind
    elif counts == [3, 2]:
        return 7, ranked_hand  # full house
    elif counts == [3, 1, 1]:
        return 4, ranked_hand  # three of a kind
    elif counts == [2, 2, 1]:
        return 3, ranked_hand  # two pairs
    elif counts == [2, 1, 1, 1]:
        return 2, ranked_hand  # one pair
    else:
        return 1, ranked_hand  # high card


def compare_poker_hands(hand_bid1, hand_bid2, p2):
    hand1, bid1 = hand_bid1
    hand2, bid2 = hand_bid2

    score1, ranked_hand1 = hand_rank(hand1, p2)
    score2, ranked_hand2 = hand_rank(hand2, p2)

    if score1 > score2:
        return -1
    elif score1 < score2:
        return 1
    else:
        for i in range(len(ranked_hand1)):
            if ranked_hand1[i] > ranked_hand2[i]:
                return -1
            elif ranked_hand1[i] < ranked_hand2[i]:
                return 1

        return 0


def cmp1(h1, h2):
    return compare_poker_hands(h1, h2, False)


def cmp2(h1, h2):
    return compare_poker_hands(h1, h2, True)


def part1(lines) -> int:
    hands = [
        (list(cards), int(bid)) for cards, bid in (line.split(" ") for line in lines)
    ]
    sorted_hands = sorted(hands, key=cmp_to_key(cmp1))
    sorted_hands.reverse()
    return sum([(i + 1) * hand[1] for i, hand in enumerate(sorted_hands)])


def part2(lines) -> int:
    hands = [
        (list(cards), int(bid)) for cards, bid in (line.split(" ") for line in lines)
    ]
    sorted_hands = sorted(hands, key=cmp_to_key(cmp2))
    sorted_hands.reverse()
    return sum([(i + 1) * hand[1] for i, hand in enumerate(sorted_hands)])


def main():
    input_txt = utils.get_input(11)
    lines = input_txt.strip().split("\n")

    print(f"Part1: {part1(lines)}")
    print(f"Part2: {part2(lines)}")


if __name__ == "__main__":
    main()
