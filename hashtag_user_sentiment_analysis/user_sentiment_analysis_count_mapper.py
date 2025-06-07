#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))  # Parse CSV row
        if len(fields) < 6:
            continue
        sentiment = fields[0].strip()       # Sentiment label (0, 2, 4)
        user = fields[4].strip().lower()    # Normalize username
        print(f"{user}\t{sentiment}")       # Emit: user \t sentiment
    except Exception:
        continue
