#!/usr/bin/env python

import math
from icecream import ic

# FILE = "sampleinput"
FILE = "input"

# manually change the ending from CRLF to LF before running this script
input = open(FILE, mode="r").read().split("\n")
lines = [line.split(": ") for line in input]

test_values = [int(line[0]) for line in lines]
list_of_list_of_numbers = [line[1].split(" ") for line in lines]
list_of_list_of_numbers = [
    [int(numbers) for numbers in list_of_numbers]
    for list_of_numbers in list_of_list_of_numbers
]  # This is ugly as sin

values = zip(test_values, list_of_list_of_numbers)

# Part 1

# values = [(7290, [6, 8, 6, 15])]
# values = [(156, [15, 6])]


def part1():
    valid = []

    for value, numbers in values:
        op_count = 2 ** (len(numbers) - 1)
        bit_shifts = int(math.log2(op_count))

        for i in range(op_count):
            accum = numbers[0]
            for bit_shift in range(bit_shifts):
                if (i >> bit_shift) % 2:
                    accum = accum + numbers[bit_shift + 1]
                else:
                    accum = accum * numbers[bit_shift + 1]

            if accum == value:
                valid.append(value)
                break

    return sum(valid)


# ic(part1())


# Part 2

# 154922241363796 was too low


def part2():
    valid = []

    for value, numbers in values:
        op_count = 3 ** (len(numbers) - 1)
        bit_shifts = len(numbers) - 1

        for i in range(op_count):
            accum = numbers[0]
            for bit_shift in range(bit_shifts):
                remainder = (i // 3**bit_shift) % 3
                match remainder:
                    case 2:
                        accum = int(str(accum) + str(numbers[bit_shift + 1]))
                    case 1:
                        accum = accum * numbers[bit_shift + 1]
                    case 0:
                        accum = accum + numbers[bit_shift + 1]

            # ic(i, remainders)
            # ic(accum)
            if accum == value:
                valid.append(value)
                break

    return sum(valid)


ic(part2())
