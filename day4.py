import hashlib

letters = 'yzbqklnj'
firstNotFound = True
for i in range(100000000):
    nextString = letters + str(i)
    hex = hashlib.md5(nextString.encode()).hexdigest()
    hex = str(hex)
    if firstNotFound and hex[:5] == '00000':
        firstNotFound = False
        print('Part 1:', i)
    if hex[:6] == '000000':
        print('Part 2:', i)
        break