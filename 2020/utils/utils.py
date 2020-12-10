#!/usr/bin/env python

import re


def sliding_window(seq, win_size, step=1):
    seq_len = len(seq)
    for i in range(0, seq_len, step):
        if i + win_size > seq_len:
            j = seq_len
        else:
            j = i + win_size
        yield seq[i:j]
        if j == seq_len:
            break


def get_input(day: int) -> str:
    filename = "input/input{:02d}".format(day)
    with open(filename, "rt") as file_input:
        return file_input.read()


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!


def positive_ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"\d+", s))  # thanks mserrano!


def floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s: str) -> list[str]:
    return re.findall(r"[a-zA-Z]+", s)


def tuple_add(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

