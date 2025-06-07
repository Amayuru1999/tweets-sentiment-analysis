#!/usr/bin/env python3
import sys
import csv
import re

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))  # Parse CSV row
        if len(fields) < 6:
            continue
        sentiment = fields[0].strip()           # Sentiment value (0, 2, 4)
        tweet = fields[5].strip().lower()       # Tweet text, lowercased
        hashtags = re.findall(r"#\w+", tweet)   # Extract hashtags
        for tag in hashtags:
            print(f"{tag}\t{sentiment}")        # Emit: hashtag \t sentiment
    except Exception:
        continue
