#!/usr/bin/python3

import sys

def main():

    running = 0
    three_kings = set()
    for cal in sys.stdin:
        if cal.isspace():
            if len(three_kings) == 3:
                small = min(three_kings)
                if small < running:
                    three_kings.remove(small)
                    three_kings.add(running)
            else:
                three_kings.add(running)
            running = 0
            continue
        running += int(cal.strip())

    print(sum(three_kings))


if __name__ == "__main__":
    main()
