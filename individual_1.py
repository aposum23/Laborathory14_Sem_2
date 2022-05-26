#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class data_type:
    first = None
    second = None

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def read(self):
        first = int(input('first: '))
        self.first = first
        second = int(input('second: '))
        self.second = second

    def display(self):
        print(f'first: {self.first}; second: {self.second}')

    def rangecheck(self, num):
        print(f'Num is: {num}')
        print(f'Num in diaposon: '
              f'{num >= self.first and num < self.second}')
        print(f'Start: {self.first}; end: {self.second}')


def main():
    diap = data_type(10, 16)
    x = random.randint(0, 20)
    diap.rangecheck(x)
    diap.display()
    diap.read()
    x = random.randint(0, 20)
    diap.rangecheck(x)


if __name__ == '__main__':
    main()
