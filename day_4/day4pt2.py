# Description: Advent of Code - Day 4 - Part 2

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

results = {}

for card in cards:
    winning_numbers = set(cards[card]['winning']).intersection(cards[card]['your'])
    if winning_numbers:
        if len(winning_numbers) == 1:
            score = 1
        else:
            score = 1
            score *= (2 ** (len(winning_numbers)-1))
    else:
         score = 0
         
    results[int(card)] = {}
    results[int(card)]['count'] = 1
    results[int(card)]['score'] = score
    results[int(card)]['winning_numbers'] = len(winning_numbers)

total_count = 0
    
for card in range(len(cards)):
    for count in range(results[card+1]['count']):
        if results[card+1]['score'] > 0:
            for index in range(results[card+1]['winning_numbers']):
                # print(f"Index: {index}")
                if index < len(cards):
                    results[card+1+index+1]['count'] += 1

for card in range(len(cards)):
    print(f"Card: {card+1}, Count: {results[card+1]['count']}")
    total_count += results[card+1]['count']
    
print(len(cards))
#print(results)
print(total_count)

# close the file
file.close()
