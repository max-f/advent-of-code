#!/usr/bin/env python

def get_input(day: int) -> str:
    filename = '/home/mfischer/git/advent-of-code/2017/input/input{:02d}'.format(day)
    with open(filename, 'rt') as file_input:
        return file_input.read()
