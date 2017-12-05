#!/usr/bin/env python

def Input(day: int) -> str:
    filename = '/home/keks/git/advent-of-code/2017/input/input{:02d}'.format(day)
    with open(filename, 'rt') as file_input:
        return file_input.read()
