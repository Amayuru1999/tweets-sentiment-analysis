#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        if len(fields) < 6:
            continue
        sentiment = fields[0].strip()
        user = fields[4].strip().lower()
        print(f"{user}\t{sentiment}")
    except Exception:
        continue
