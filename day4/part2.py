#!/usr/bin/python3

import sys

def main():

    count = 0
    for line in sys.stdin:
        sections = line.strip().replace(',','-').split('-')
        sections = list(map(int, sections))
        if (sections[0] <= sections[2] and sections[1] >= sections[2]) or (sections[0] >= sections [2] and sections[0] <= sections[3]):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
