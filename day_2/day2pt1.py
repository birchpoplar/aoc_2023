# Description : Advent Of Code 2020 : Day 2, Part 1

import re

# open file
f = open("input.txt", "r")

# read file
lines = f.readlines()

# Pattern to match the game ID and the color counts
game_pattern = r'Game (\d+): (.+?)\s*(?=Game|$)'

# Pattern to match individual color counts
color_pattern = r'(\d+) (green|blue|red)'

# Dictionary to store the extracted data
games_data = {}

game = re.findall(game_pattern, lines, re.DOTALL)

for game_id, data in game:
    # Dictionary to store color counts for each game
    color_counts = {'green': [], 'blue': [], 'red': []}
    
    # Split the data into sets based on semi-colons
    sets = data.split(';')

    for set_data in sets:
        # Find all color counts in this set
        colors = re.findall(color_pattern, set_data)

        for count, color in colors:
            color_counts[color].append(int(count))

    games_data[game_id] = color_counts

print(games_data)

# close file
f.close()
