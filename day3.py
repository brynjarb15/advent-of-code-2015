import pprint
pp = pprint.PrettyPrinter(indent=4, width=500)

# Read the input
f = open("input3.txt", "r")
lines = f.read().splitlines()

line = lines[0]
x = 0
y = 0
coords = set()
for arrow in line:
    if arrow == '^':
        y += 1
    if arrow == 'v':
        y -= 1
    if arrow == '<':
        x -= 1
    if arrow == '>':
        x += 1
    coords.add((x, y))
print('Part1:', len(coords))


x = 0
y = 0
roboX = 0
roboY = 0
coords = set()
for arrow in line[::2]:
    if arrow == '^':
        y += 1
    elif arrow == 'v':
        y -= 1
    elif arrow == '>':
        x += 1
    elif arrow == '<':
        x -= 1
    coords.add((x, y))

for arrow in line[1::2]:
    if arrow == '^':
        roboY += 1
    elif arrow == 'v':
        roboY -= 1
    elif arrow == '>':
        roboX += 1
    elif arrow == '<':
        roboX -= 1
    coords.add((roboX, roboY))

print('Part1:', len(coords))



# 1348 is too low
# 2640 is too high