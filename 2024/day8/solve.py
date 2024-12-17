#!/usr/bin/env python

import re
from itertools import permutations, combinations
from icecream import ic

# Sample Input is 12x12
# Input is 50x50

# FILE = "sampleinput"
FILE = "input"

# manually change the ending from CRLF to LF before running this script
input = open(FILE, mode="r").read().split("\n")
MATRIX = [[char for char in row] for row in input]
BOUNDS = len(MATRIX)  # since it's a square anyways, I'm gonna be lazy here

# Part 1

# each frequency is indicated by a single lowercase letter, uppercase letter, or digit
pattern = re.compile("\\w")

antennas: dict = {}

for y, row in enumerate(MATRIX):
    for x, element in enumerate(row):
        found = pattern.findall(element)

        if found:
            key = found[0]
            if antennas.get(key):
                antennas[key].append((x, y))
            else:
                antennas[key] = [(x, y)]


# return taxicab distance
def taxicab_distance(loc1, loc2):
    (x1, y1) = loc1
    (x2, y2) = loc2
    return (x1 - x2, y1 - y2)


def taxicab_sum(loc1, loc2):
    (x1, y1) = loc1
    (x2, y2) = loc2
    return (x1 + x2, y1 + y2)


def taxicab_sub(loc1, loc2):
    (x1, y1) = loc1
    (x2, y2) = loc2
    return (x1 - x2, y1 - y2)


# check if element is within bounds
def within_bounds_check(loc, bounds=BOUNDS):
    (x, y) = loc
    return not (x < 0 or x >= BOUNDS or y < 0 or y >= BOUNDS)


def part1():
    antinodes = set()

    for freq, locs in antennas.items():
        combs = list(combinations(locs, 2))

        for comb in combs:
            (loc1, loc2) = comb
            dist = taxicab_distance(loc1, loc2)

            antinodes.add(taxicab_sum(loc1, dist))
            antinodes.add(taxicab_sub(loc2, dist))

    antinodes = {antinode for antinode in antinodes if within_bounds_check(antinode)}
    return len(antinodes)


ic(part1())


def part2():
    antinodes = set()

    for freq, locs in antennas.items():
        combs = list(combinations(locs, 2))

        for comb in combs:
            (loc1, loc2) = comb
            dist = taxicab_distance(loc1, loc2)
            newloc1 = loc1
            newloc2 = loc2
            antinodes.add(newloc1)
            antinodes.add(newloc2)

            for _ in range(BOUNDS):
                newloc1 = taxicab_sum(newloc1, dist)
                newloc2 = taxicab_sub(newloc2, dist)
                antinodes.add(newloc1)
                antinodes.add(newloc2)

    antinodes = {antinode for antinode in antinodes if within_bounds_check(antinode)}
    return len(antinodes)


ic(part2())
