# Description: Advent of Code - Day 1, part 2

def chkNumText(str, index):
    if str[index:index+3] == "one":
        return 1, 3
    elif str[index:index+3] == "two":
        return 2, 3
    elif str[index:index+5] == "three":
        return 3, 5
    elif str[index:index+4] == "four":
        return 4, 4
    elif str[index:index+4] == "five":
        return 5, 4
    elif str[index:index+3] == "six":
        return 6, 3
    elif str[index:index+5] == "seven":
        return 7, 5
    elif str[index:index+5] == "eight":
        return 8, 5
    elif str[index:index+4] == "nine":
        return 9, 4
    else:
        return False, False

# open file input.txt
f = open("input.txt", "r")
lines = f.readlines()

first = 0
last = 0
total = 0
substr = ""

# read line by line
for line in lines:
    for i in range(len(line)):
        if line[i].isnumeric():
            if first == 0:
                first = line[i]
                last = line[i]
            else:
                last = line[i]
        if line[i].isalpha():
            val, length = chkNumText(line, i)
            if val != False:
                if first == 0:
                    first = val
                    last = val
                else:
                    last = val
                i += length

    num = (int(first) * 10) + int(last)        
    total += num
    print(f"line: {line[:-1]}, first: {first}, last: {last}, num: {num}")
    first = 0
    last = 0

    
print(f"total: {total}")

# close file
f.close()



