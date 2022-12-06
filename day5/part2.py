#!/usr/bin/python3

import sys


def output(crates):

    for item in crates:
        print(crates[item][0])


def operation(crates, num, start, end):

    move = []
    for i in range(num):
        move.append(crates[start].pop(0))

    for i in range(num):
        item = move.pop(-1)
        crates[end].insert(0, item)


def main():

    crates = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [],
            '8': [], '9': []}
    for line in sys.stdin:
        if line[0].isspace(): break
        offset = 0
        for i,c in enumerate(line.rstrip()):
            if c.isalpha():
                crates[str(offset)].append(c)
            if not i % 4:
                offset += 1
    offset = input()

    for line in sys.stdin:
        cmd = line.rstrip().split()
        operation(crates, int(cmd[1]), cmd[3], cmd[5])

    output(crates)

if __name__ == '__main__':
    main()
