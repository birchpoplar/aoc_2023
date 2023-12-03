# Description : Advent of Code - Day 3, part 1

import re
import string
import itertools

def is_symbol(char):
    # Check if the character is a punctuation mark
    if char in string.punctuation:
        # Return True if it's not a period
        return char != '.'
    return False

def chk_neighbours_for_symbols(schematic, row, col):
#   print(f"Checking row: {row} col: {col}")
    x_moves = [0, -1, 1]
    y_moves = [0, -1, 1]
    neighbours = list(itertools.product(x_moves, y_moves))
#    print(neighbours)
    for x, y in neighbours:
        new_row, new_col = row+y, col+x
        if 0 <= new_row < len(schematic) and 0 <= new_col < len(schematic[new_row]):
#            print(f"x: {new_col}, y: {new_row}, neighbour: {schematic[new_row][new_col]}, is_symbol: {is_symbol(schematic[new_row][new_col])}")
            if is_symbol(schematic[new_row][new_col]):
                return True
    return False
        
# open file input.txt
f = open("input.txt", "r")

# read line by line
schematic = f.readlines()

number_locs_line = {}
number_locs_schematic = {}
line_num = 0

for line in schematic:
    for match in re.finditer(r'\d+', line.rstrip()):
        start_pos = match.start()
        number = match.group()
        number_locs_line[start_pos] = number

    number_locs_schematic[line_num] = number_locs_line
    number_locs_line = {}
    line_num += 1

# Now we have a dictionary of dictionaries, where the key is the line number, and the value is a dictionary of the number locations and values

part_numbers = []

for line in number_locs_schematic:
    for entry in number_locs_schematic[line]:
#        print(f"line: {line}, entry: {entry}, number: {number_locs_schematic[line][entry]}")
        number_valid = False
#        print(f"Checking number: {number_locs_schematic[line][entry]}")
        for digit in range(len(str(number_locs_schematic[line][entry]))):
#            print(f"digit: {digit}")
            if number_valid:
                continue
            if chk_neighbours_for_symbols(schematic, line, entry+digit):
#                print(f"Number has symbol: {number_locs_schematic[line][entry]}")
                number_valid = True
                part_numbers.append(int(number_locs_schematic[line][entry]))

# print(part_numbers)
print(sum(part_numbers))
