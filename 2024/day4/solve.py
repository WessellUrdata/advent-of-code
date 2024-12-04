#!/usr/bin/env python

from icecream import ic
import numpy as np

# FILE = "sampleinput"
FILE = "input"

word_search = open(FILE, mode="r").read().split("\n")
matrix = np.array([[char for char in row] for row in word_search])

# ic(matrix)


# Part 1
# I very much didn't need NumPy for this
# Yes, this is an absolute mess, I'll try a better way in Part 2

l2r_strings = [["".join(l2r[i : i + 4]) for i, x in enumerate(l2r)] for l2r in matrix]
l2r_flatten = [item for row in l2r_strings for item in row]
l2r_count = l2r_flatten.count("XMAS") + l2r_flatten.count("SAMX")


r2l_matrix = np.fliplr(matrix)


t2b_matrix = np.transpose(matrix)
t2b_strings = [
    ["".join(t2b[i : i + 4]) for i, x in enumerate(t2b)] for t2b in t2b_matrix
]
t2b_flatten = [item for row in t2b_strings for item in row]
t2b_count = t2b_flatten.count("XMAS") + t2b_flatten.count("SAMX")


b2t_matrix = np.transpose(np.flipud(matrix))


tl2br_matrix = [np.diag(matrix, k=i) for i in range(-len(matrix), len(matrix))]
tl2br_strings = [
    ["".join(tl2br[i : i + 4]) for i, x in enumerate(tl2br)] for tl2br in tl2br_matrix
]
tl2br_flatten = [item for row in tl2br_strings for item in row]
tl2br_count = tl2br_flatten.count("XMAS") + tl2br_flatten.count("SAMX")


bl2tr_matrix = [
    np.diag(b2t_matrix, k=i) for i in range(-len(t2b_matrix), len(t2b_matrix))
]
bl2tr_strings = [
    ["".join(bl2tr[i : i + 4]) for i, x in enumerate(bl2tr)] for bl2tr in bl2tr_matrix
]
bl2tr_flatten = [item for row in bl2tr_strings for item in row]
bl2tr_count = bl2tr_flatten.count("XMAS") + bl2tr_flatten.count("SAMX")


# ic(l2r_count + t2b_count + tl2br_count + bl2tr_count)


# Part 2
# You know, this reminds me a lot of convolution

conv = np.array(
    [
        [matrix[y - 1 : y + 2, x - 1 : x + 2] for x in range(1, len(matrix) - 1)]
        for y in range(1, len(matrix) - 1)
    ]
).reshape(-1, 3, 3)

count = 0

for x in conv:
    if (
        x[1][1] == "A"
        and ((x[0][0] == "M" and x[2][2] == "S") or (x[0][0] == "S" and x[2][2] == "M"))
        and ((x[2][0] == "M" and x[0][2] == "S") or (x[2][0] == "S" and x[0][2] == "M"))
    ):
        count = count + 1

ic(count)
