#!/usr/bin/python3

import sys

UPPER=38
LOWER=96

def letter_val(first, second):

    for i in first:
        if i in second:
            if i.isupper():
                return ord(i)-UPPER
            else:
                return ord(i)-LOWER


def main():

    priority = 0
    for line in sys.stdin:
        line = line.strip()
        part1 = set(line[:len(line)//2])
        part2 = set(line[len(line)//2:])
        priority += letter_val(part1, part2)

    print(priority)

if __name__ == '__main__':
    main()
