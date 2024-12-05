#!/usr/bin/env python

from icecream import ic

# FILE = "sampleinput"
FILE = "input"

# manually change the ending from CRLF to LF before running this script
input = open(FILE, mode="r").read().split("\n")
input_separator = input.index("")

rules_raw = input[:input_separator]
updates_raw = input[input_separator + 1 :]

rules = [[int(rule) for rule in rule_raw.split("|")] for rule_raw in rules_raw]
updates = [
    [int(update) for update in update_raw.split(",")] for update_raw in updates_raw
]
count = 0

# Part 1


def isCorrect(update):
    return all(
        [
            all([page, right_element] in rules for right_element in update[index + 1 :])
            for index, page in enumerate(update)
        ]
    )


# ic(sum([update[len(update) // 2] for update in updates if isCorrect(update)]))

# Part 2

incorrects = [update for update in updates if not isCorrect(update)]

for update in updates:
    for index, page in enumerate(update):
        for right_element in update[index + 1 :]:
            right_element_index = update.index(right_element)
            if [page, right_element] not in rules:
                update[right_element_index], update[index] = page, right_element
                page = right_element  # Modifying page in place is bad! (introduces side-effect) But it works for our case

ic(sum([incorrect[len(incorrect) // 2] for incorrect in incorrects]))
