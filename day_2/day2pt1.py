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

for line in lines:
    # Find all games in the line

    game = re.findall(game_pattern, line, re.DOTALL)

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

possible_games = []

for key in games_data.keys():
    # Get the color counts for this game
    color_counts = games_data[key]

    if max(color_counts['green']) > 13:
        continue
    if max(color_counts['blue']) > 14:
        continue
    if max(color_counts['red']) > 12:
        continue
    possible_games.append(int(key))

print("Possible games: ")
print(possible_games)
print("Total of possible games: ")
print(sum(possible_games))
        
# close file
f.close()
