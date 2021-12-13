import pprint
pp = pprint.PrettyPrinter(indent=4, width=500)

# Read the input
f = open("input1.txt", "r")
lines = f.read().splitlines()

line = lines[0]

open = line.count('(')
close = line.count(')')
print('Part 1:', open - close)

floor = 0
for index, s in enumerate(line):
    if floor < 0:
        print('Part 2:', index)
        break
    if s == '(':
        floor += 1
    elif s == ')':
        floor -= 1

