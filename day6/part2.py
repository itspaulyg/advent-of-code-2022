#!/usr/bin/python3

import sys


def main():

    buffer = input()
    holding = []
    for i in buffer:
        holding.append(i)
        if len(holding) > 13:
            if len(set(holding[-14:])) == 14:
                print(len(holding))
                break

if __name__ == '__main__':
    main()
