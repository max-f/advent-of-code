#!/usr/bin/env python

from utils import utils
from collections import deque


def swap(letters: list, a: int, b: int) -> list:
    letters[b], letters[a] = letters[a], letters[b]
    return letters


def exec_moves(day: int, letters: list) -> None:
    # letters = ['a', 'b', 'c', 'd', 'e']
    moves = utils.get_input(day)
    # moves = 's1,x3/4,pe/b'
    # Look for cycle and as soon as found: return state of cycle at 10 ** 9th iteration
    done = []
    for i in range(10 ** 9):
        letters_str = ''.join(letters)
        if letters_str in done:
            print('Part 2: {0}'.format(done[10 ** 9 % i]))
            return

        done.append(letters_str)

        for move in moves.strip().split(','):
            if move and move[0] == 's':
                letters = deque(letters)
                letters.rotate(int(move[1:]))
                letters = list(letters)
            elif move and move[0] == 'x':
                idcs = move[1:].split('/')
                letters = swap(letters, int(idcs[0]), int(idcs[1]))
            elif move and move[0] == 'p':
                letters = swap(letters, letters.index(move[1]), letters.index(move[-1]))
        if i == 0:
            print('Part 1: {0}'.format(''.join(letters)))


def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    exec_moves(16, letters)


if __name__ == '__main__':
    main()
