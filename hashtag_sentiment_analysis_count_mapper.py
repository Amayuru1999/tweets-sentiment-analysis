#!/usr/bin/env python3
import sys
import csv
import re

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        if len(fields) < 6:
            continue
        sentiment = fields[0].strip()
        tweet = fields[5].strip().lower()
        hashtags = re.findall(r"#\w+", tweet)
        for tag in hashtags:
            print(f"{tag}\t{sentiment}")
    except Exception:
        continue
