#!/usr/bin/python3

import sys

UPPER=38
LOWER=96

def letter_val(first, second, third):

    for i in first:
        if i in third and i in second:
            if i.isupper():
                return ord(i)-UPPER
            else:
                return ord(i)-LOWER

def main():

    priority = 0
    group = []
    for line in sys.stdin:
        group.append(line.rstrip())
        if not len(group) % 3:
            priority += letter_val(set(group[0]), set(group[1]), set(group[2]))
            group = []

    print(priority)

if __name__ == '__main__':
    main()
