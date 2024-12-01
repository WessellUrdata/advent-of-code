# /usr/bin/env python

# I tried using Bash and awk to do it, but I just couldn't
# and yes, this is a terrible solution

import csv
from icecream import ic

FILENAME = "input"

with open(FILENAME) as csvfile:
    rows = [
        [item for item in row if item != ""]
        for row in csv.reader(csvfile, delimiter=" ")
    ]
    col0 = sorted([int(col[0]) for col in rows])
    col1 = sorted([int(col[1]) for col in rows])


# Part 1

dist = 0

for x in range(len(col0)):
    dist += abs(col0[x] - col1[x])

ic(dist)


# Part 2

col1Freq = {c: col1.count(c) for c in col1}

similarityScore = 0

for i in col0:
    similarityScore += i * col1.count(i)

ic(similarityScore)
