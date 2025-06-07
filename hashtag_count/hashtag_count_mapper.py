#!/usr/bin/env python3

import sys
import re

# Process each line from standard input
for line in sys.stdin:
    hashtags = re.findall(r"#\w+", line.lower())
    for tag in hashtags:
        print(f"{tag}\t1")  # Emit each hashtag with count 1
