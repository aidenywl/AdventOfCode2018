from typing import List
from typing import Tuple
import re


def part1(input_data: List[str]):
    # create a hashmap What's the cost-benefit to either? with default value of 0
    cloth_grid = {}

    for command in input_data:
        cut_positions = parse_cuts(command)
        increment_cut(cloth_grid, cut_positions)

    counter = 0
    # then, loop through the entire area and sum up those with two or more.
    for value in cloth_grid.values():
        if value > 1:
            counter +=1

    return counter


def parse_cuts(cut_design: str):
    cut_information = list(map(int, re.findall('\d+', cut_design)))
    # return a list of the cuts in tuples.
    starting_position = (cut_information[1], cut_information[2])
    length = cut_information[3]
    width = cut_information[4]
    return generate_tuples(starting_position, length, width)


def generate_tuples(starting_position, length: int, width: int):
    ending_length_axis = starting_position[0] + length
    ending_width_axis = starting_position[1] + width

    cuts = []
    for current_length in range(starting_position[0], ending_length_axis):
        for current_width in range(starting_position[1], ending_width_axis):
            cuts.append((current_length, current_width))
    return cuts


def increment_cut(cloth_grid, cut_positions: List[Tuple[int, int]]):
    for cut in cut_positions:
        if cut not in cloth_grid:
            cloth_grid[cut] = 1
        else:
            cloth_grid[cut] += 1


if __name__ == "__main__":
    part1_input = open("input1.txt", 'r')
    print(f"The answer to part 1 is: {part1(part1_input.read().splitlines())}")
