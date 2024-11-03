import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# These functions take an input of a list of class of Books and sorts the list, alphabetically, by title.
def index_smallest_from_alpha(values:list[data.Book], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title < values[mindex].title:
            mindex = idx

    return mindex

def selection_sort_alpha(values:list[data.Book]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from_alpha(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 2
# This function takes an input of a str and gives an output of a str after it has swapped uppercase characters
# to lowercase letters.
def swap_case(input_str:str) -> str:
    output = ""
    for char in input_str:
        if char.islower():
            output += char.upper()
        elif char.isupper():
            output += char.lower()
        else:
            output += char
    return output


# Part 3
# This function takes an input of 3 strings. The first one is the subject, the second input is a character you
# want replaced in the subject, and the third input is what you want the old character to be replaced with.
# This is then outputted as a string.
def str_translate(input_str:str, old:str, new:str) -> str:
    output_str = ""
    for char in input_str:
        if char == old:
            output_str += new
        else:
            output_str += char
    return output_str

# Part 4
# This function takes an input of str and outputs a count of how many times each word in the string appears and
# outputs it as a dictionary.
def histogram(input_str:str) -> dict[str, int]:
    output_dict = {}
    split = str.split(input_str)
    for word in split:
        if word not in output_dict:
            output_dict[word] = 1
        else:
            output_dict[word] += 1
    return output_dict
