from typing import List
from itertools import combinations

# Advent of code for day 2.


def part_1(input_data: List[str]):
    # store a set of twos
    # store a set of threes
    letters_appeared_twice, letters_appeared_thrice = 0, 0

    # iterate through the input data and get counts of 2 and 3.
    for box_id in input_data:
        box_id = box_id.lower()
        alphabet_count = count_alphabets(box_id.lower())

        letter_counts = alphabet_count.values()

        if 2 in letter_counts:
            letters_appeared_twice += 1

        if 3 in letter_counts:
            letters_appeared_thrice += 1

    # multiply the count of two and 3 together and return it.

    return letters_appeared_thrice * letters_appeared_twice


def part_2(input_data: List[str]):
    for id1, id2 in combinations(input_data, 2):

        # calculate hamming distance.
        if hamming_distance(id1, id2) == 1:
            # remove the digit and return it.
            return find_same_alphabets(id1, id2)


def hamming_distance(string1, string2):

    # zipping the two strings into an iterable
    iterable_string_tuple = zip(string1, string2)

    # return 1 if they are not equal
    return sum(char1 != char2 for char1, char2 in iterable_string_tuple)


def find_same_alphabets(string1, string2):
    result = list(string1)
    counter = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            result[counter] = ""

        counter += 1

    return "".join(result)


def count_alphabets(input_string: str):
    alphabet_count = {}
    for char in input_string:
        keys = alphabet_count.keys()
        if char in keys:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

    return alphabet_count


# define helper method that takes in a string.
    # iterate over each char.
    # for each char, place it into the hash table and increase the count by 1.

if __name__ == "__main__":
    input_1 = open("input1.txt",'r')
    print(f"The answer to part 1 is:{part_1(input_1.read().splitlines())}")
    input_2 = open("input1.txt", 'r')
    print(f"The answer to part 2 is: {part_2(input_2.read().splitlines())}")