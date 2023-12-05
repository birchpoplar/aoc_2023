# Description: Advent of Code - Day 4 - Part 1

import re

def parse_line(line):
    # Extract the card number using regex
    card_number_match = re.match(r'Card\s+(\d+):', line)
    if not card_number_match:
        raise ValueError(f"Card number not found in line: '{line}'")
    card_number = card_number_match.group(1)

    # Split the line at the pipe
    _, values = line.split(':')
    left_values, right_values = values.split('|')

    # Extract numbers from each part
    left_numbers = [int(num) for num in re.findall(r'\d+', left_values)]
    right_numbers = [int(num) for num in re.findall(r'\d+', right_values)]

    # Return a dictionary with these numbers
    return {card_number: {'winning': left_numbers, 'your': right_numbers}}

# Open and read the file
file_path = 'input.txt'
with open(file_path, 'r') as file:
    cards = {}
    for line in file:
        card_data = parse_line(line.strip())
        cards.update(card_data)

# cards now contains the parsed data
# print(cards)

sum_scores = 0

for card in cards:
    winning_numbers = set(cards[card]['winning']).intersection(cards[card]['your'])
    if winning_numbers:
        if len(winning_numbers) == 1:
            score = 1
        else:
            score = 1
            score *= (2 ** (len(winning_numbers)-1))
        print(f"Card: {card}, Numbers: {winning_numbers}, Score: {score}")
        sum_scores += score

print(f"Sum of scores: {sum_scores}")

# close the file
file.close()
