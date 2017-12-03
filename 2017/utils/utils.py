#!/usr/bin/env python

def Input(day: int) -> str:
    filename = '/home/keks/git/advent_of_code/2017/input/input{}'.format(day)
    with open(filename, 'rt') as file_input:
        return file_input.read()
