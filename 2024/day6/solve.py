#!/usr/bin/env python

import copy
from enum import Enum
from icecream import ic

# FILE = "sampleinput"
FILE = "input"

# manually change the ending from CRLF to LF before running this script
input = open(FILE, mode="r").read().split("\n")
matrix = [[char for char in row] for row in input]

MAP_SIZE = len(matrix)  # the map is a square so it's fine

((pos_x, pos_y),) = [
    (row.index("^"), index) for index, row in enumerate(matrix) if "^" in row
]

Directions = Enum(
    value="Directions",
    names=[("UP", (0, -1)), ("RIGHT", (1, 0)), ("DOWN", (0, 1)), ("LEFT", (-1, 0))],
)
direction = Directions.UP


def move(pos, dir):
    (pos_x, pos_y) = pos
    (dir_x, dir_y) = dir.value
    return (pos_x + dir_x, pos_y + dir_y)


def out_of_bounds(pos_x, pos_y):
    if (pos_x < 0 or pos_x >= MAP_SIZE) or (pos_y < 0 or pos_y >= MAP_SIZE):
        return True
    else:
        return False


visited_pos = set()


# Part 1
def part1(pos_x, pos_y, direction):
    (next_pos_x, next_pos_y) = (0, 0)

    def is_obstacle(pos_x, pos_y):
        if matrix[pos_y][pos_x] == "#":
            return True
        else:
            return False

    while not out_of_bounds(next_pos_x, next_pos_y):
        if is_obstacle(next_pos_x, next_pos_y):
            match direction:
                case Directions.UP:
                    direction = Directions.RIGHT

                case Directions.RIGHT:
                    direction = Directions.DOWN

                case Directions.DOWN:
                    direction = Directions.LEFT

                case Directions.LEFT:
                    direction = Directions.UP

        else:
            (pos_x, pos_y) = move((pos_x, pos_y), direction)
            visited_pos.add((pos_x, pos_y))

        (next_pos_x, next_pos_y) = move((pos_x, pos_y), direction)

    return len(visited_pos)


# ic(part1(pos_x, pos_y, direction))
part1(pos_x, pos_y, direction)

# Part 2

available_obstacles = visited_pos
# available_obstacles.remove((pos_x, pos_y))


def part2(x, y, dir):
    stuck: list = []

    for obs_x, obs_y in available_obstacles:
        test_matrix = copy.deepcopy(matrix)
        test_matrix[obs_y][obs_x] = "#"
        # ic(test_matrix)

        def is_obstacle(pos_x, pos_y):
            if test_matrix[pos_y][pos_x] == "#":
                return True

        pos_x = x
        pos_y = y
        direction = dir

        turn_point: list = []

        (next_pos_x, next_pos_y) = move((x, y), dir)

        while not out_of_bounds(next_pos_x, next_pos_y):
            if is_obstacle(next_pos_x, next_pos_y):
                match direction:
                    case Directions.UP:
                        direction = Directions.RIGHT

                    case Directions.RIGHT:
                        direction = Directions.DOWN

                    case Directions.DOWN:
                        direction = Directions.LEFT

                    case Directions.LEFT:
                        direction = Directions.UP
                turn_point.append((pos_x, pos_y))
                if len(turn_point) >= 400:
                    break

            else:
                (pos_x, pos_y) = move((pos_x, pos_y), direction)

            (next_pos_x, next_pos_y) = move((pos_x, pos_y), direction)

        # This is literally just guessing
        if len(turn_point) >= 400:
            stuck.append(True)
        else:
            stuck.append(False)

    ic(sum(stuck))


part2(pos_x, pos_y, direction)
