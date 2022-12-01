#!/usr/bin/python3

import sys

def main():

    running = 0
    high = 0
    for cal in sys.stdin:
        if cal.isspace():
            high = high if high > running else running
            running = 0
            continue
        running += int(cal.strip())

    print(high)


if __name__ == "__main__":
    main()
