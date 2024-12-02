#!/usr/bin/env python

import copy
import operator
from icecream import ic

FILE = "input"

# use LF for file ending for input, please
with open(FILE, mode="r") as f:
    reports = [
        [int(level) for level in report.split(" ")] for report in f.read().split("\n")
    ]

# ic(reports)


# Part 1

diffs = [list(map(operator.sub, levels[:-1], levels[1:])) for levels in reports]

safeLevels = [
    diff
    for diff in diffs
    if (all(i <= -1 and i >= -3 for i in diff) or all(i >= 1 and i <= 3 for i in diff))
]

# ic(len(safeLevels))


# Part 2

newReports = [[copy.copy(levels) for _ in levels] for levels in reports]

# remove the index-0 element for 0-th array, etc
[[newLevel[x].pop(x) for x in range(len(newLevel))] for newLevel in newReports]

newDiffsArray = [
    [list(map(operator.sub, levels[:-1], levels[1:])) for levels in newLevels]
    for newLevels in newReports
]

newSafeLevels = [
    [
        diff
        for diff in newDiffs
        if (
            all(i <= -1 and i >= -3 for i in diff)
            or all(i >= 1 and i <= 3 for i in diff)
        )
    ]
    for newDiffs in newDiffsArray
]

newSafeLevels = [result for result in newSafeLevels if result != []]

ic(len(newSafeLevels))
