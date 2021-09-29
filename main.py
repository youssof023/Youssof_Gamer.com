list = [5, 4, 4, 3, 1, -2, -3, -5]

total = 0
num = 0

while list[num] > 0:
    total += list[num]
    num += list[num]

print(total)