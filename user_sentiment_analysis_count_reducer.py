#!/usr/bin/env python3
import sys

current_user = None
counts = {"0": 0, "2": 0, "4": 0}  # Negative, Neutral, Positive
header_printed = False

# Column width definitions
USER_COL_WIDTH = 20
COL_WIDTH = 10

def format_line(user, pos, neu, neg):
    return f"{user.ljust(USER_COL_WIDTH)}{str(pos).ljust(COL_WIDTH)}{str(neu).ljust(COL_WIDTH)}{str(neg).ljust(COL_WIDTH)}"

for line in sys.stdin:
    try:
        user, sentiment = line.strip().split("\t")

        if not header_printed:
            print(format_line("User", "Positive", "Neutral", "Negative"))
            header_printed = True

        if user != current_user:
            if current_user:
                print(format_line(current_user, counts['4'], counts['2'], counts['0']))
            current_user = user
            counts = {"0": 0, "2": 0, "4": 0}

        if sentiment in counts:
            counts[sentiment] += 1

    except Exception:
        continue

if current_user:
    print(format_line(current_user, counts['4'], counts['2'], counts['0']))
