#!/usr/bin/env python


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
