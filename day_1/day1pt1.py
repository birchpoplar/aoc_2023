# Description: Advent of Code - Day 1, part 1

# open file input.txt
f = open("input.txt", "r")
lines = f.readlines()

first = 0
last = 0
total = 0

# read line by line
for line in lines:
    for char in line:
        if char.isnumeric():
            if first == 0:
                first = char
                last = char
            else:
                last = char
    num = (int(first) * 10) + int(last)        
    total += num
    print(f"first: {first}, last: {last}, num: {num}")
    first = 0
    last = 0

print(f"total: {total}")

# close file
f.close()
