#!/usr/bin/python3
"""Log parsing reads a stdin line by line and computes metrics"""

import fileinput
from typing import List


line_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

for line in fileinput.input():
    ln = line.split()

    if len(ln) != 9:
        continue

    line_count += 1
    total_size += int(ln[8])

    if int(ln[7]) in status_codes.keys():
        status_codes[int(ln[7])] += 1
    if line_count == 10:
        print("File size: {}".format(total_size))
        for key in sorted(status_codes.keys()):
            print("{}: {}".format(key, status_codes[key]))

        line_count = 0
        total_size = 0
