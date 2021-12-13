import pprint
pp = pprint.PrettyPrinter(indent=4, width=500)

# Read the input
f = open("input2.txt", "r")
lines = f.read().splitlines()


lines = lines
count = 0
ribbonCount = 0
for line in lines:
    sides = line.split('x')
    sides = [int(j) for j in sides]
    sides.sort()
    a = sides[0]
    b = sides[1]
    c = sides[2]
    s = [a*b, a*c, b*c]
    slack = min(s)
    s = [i*2 for i in s]
    count += sum(s)+ slack

    # Ribbon part
    wrap = 2*a + 2*b
    bow = a*b*c
    ribbonCount += wrap + bow


print('Part1:', count)
print('Part2:', ribbonCount)


