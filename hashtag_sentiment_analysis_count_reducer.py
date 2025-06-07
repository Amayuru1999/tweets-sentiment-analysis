#!/usr/bin/env python3
import sys

current_tag = None
counts = {"0": 0, "2": 0, "4": 0}  # Negative, Neutral, Positive
header_printed = False

# Column widths
TAG_WIDTH = 30
COL_WIDTH = 10

def format_line(tag, pos, neu, neg):
    return f"{tag.ljust(TAG_WIDTH)}{str(pos).ljust(COL_WIDTH)}{str(neu).ljust(COL_WIDTH)}{str(neg).ljust(COL_WIDTH)}"

for line in sys.stdin:
    try:
        tag, sentiment = line.strip().split("\t")

        if not header_printed:
            print(format_line("Hashtag", "Positive", "Neutral", "Negative"))
            header_printed = True

        if tag != current_tag:
            if current_tag:
                print(format_line(current_tag, counts["4"], counts["2"], counts["0"]))
            current_tag = tag
            counts = {"0": 0, "2": 0, "4": 0}

        if sentiment in counts:
            counts[sentiment] += 1

    except Exception:
        continue

if current_tag:
    print(format_line(current_tag, counts["4"], counts["2"], counts["0"]))
