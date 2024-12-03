#!/usr/bin/env python

import re
from icecream import ic

# FILE = "sampleinput"
# FILE = "sampleinput2"
FILE = "input"

# use LF for file ending for input, please
memory = open(FILE, mode="r").read()


# Part 1
mulRegex = "mul\\(\\d+,\\d+\\)"
instructions = re.findall(mulRegex, memory)
numbers = [re.findall("\\d+", digits) for digits in instructions]

multipliedNumbers = [int(digit[0]) * int(digit[1]) for digit in numbers]
# ic(sum(multipliedNumbers))


# Part 2
combinedRegex = "mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)"
combinedInstructions = re.findall(combinedRegex, memory)

donts = [
    i for i, instruction in enumerate(combinedInstructions) if instruction == "don't()"
]
dos = [i for i, instruction in enumerate(combinedInstructions) if instruction == "do()"]

correctedInstructions = []
currentInst = "do()"

for index, inst in enumerate(combinedInstructions):
    if inst == "don't()" or inst == "do()":
        currentInst = inst
    else:
        if currentInst == "do()":
            correctedInstructions.append(inst)


correctedNumbers = [re.findall("\\d+", digits) for digits in correctedInstructions]
multipliedNumbers = [int(digit[0]) * int(digit[1]) for digit in correctedNumbers]
ic(sum(multipliedNumbers))
