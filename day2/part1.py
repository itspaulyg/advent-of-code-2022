#!/usr/bin/python3

import sys

STRAT = {'AX': 4, 'BX': 1, 'CX': 7, 'AY': 8, 'BY': 5, 'CY': 2, 'AZ': 3, 'BZ':
        9, 'CZ': 6}


def main():
    score = 0
    for line in sys.stdin:
        score += STRAT[line.replace(' ', '').strip()]

    print(score)

if __name__ == '__main__':
    main()
