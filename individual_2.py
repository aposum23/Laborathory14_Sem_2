#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime


class Time:
    hours = None
    minutes = None
    seconds = None

    def __init__(self, h, m, s):
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

    def read(self):
        h = input('Hours: ')
        self.hours = int(h)
        m = input('Minutes: ')
        self.minutes = int(m)
        s = input('Seconds: ')
        self.seconds = int(s)

    def display(self):
        print(f'Time: {self.hours}:{self.minutes}:{self.seconds}')

    def change_time(self, *arg):
        if type(arg[0]) == type(' '):
            arg = arg[0].split(':')
            self.hours = arg[0]
            self.minutes = arg[1]
            self.seconds = arg[2]
        elif type(arg[0]) == type(0):
            self.hours = arg[0]
            self.minutes = arg[1]
            self.seconds = arg[2]
        elif type(arg[0]) == type(datetime.time(1,1,1)):
            arg = str(arg[0])
            arg = arg.split(':')
            self.hours = arg[0]
            self.minutes = arg[1]
            self.seconds = arg[2]


def main():
    tm = Time(16, 7, 0)
    tm.display()
    tm.read()
    tm.display()
    tm.change_time(16, 8, 0)
    tm.display()
    tm.change_time('16:9:30')
    tm.display()
    tm.change_time(datetime.time(16, 10, 21))
    tm.display()


if __name__ == "__main__":
    main()
