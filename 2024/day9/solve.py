#!/usr/bin/env python

from icecream import ic

# FILE = "sampleinput"
FILE = "input"

# manually change the ending from CRLF to LF before running this script
input = open(FILE, mode="r").read()

digits = [digit for digit in input]
ic(len(digits))
