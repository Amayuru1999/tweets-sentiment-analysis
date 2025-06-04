#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    hashtags = re.findall(r"#\w+", line.lower())
    for tag in hashtags:
        print(f"{tag}\t1")
