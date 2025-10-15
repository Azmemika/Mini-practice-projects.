from numpy import *
import random
import numpy as np

size = int(input("Enter the size of the matrix (n x n): "))

max_twos = (size * size) // 4

matrixreal = np.random.choice([1], size=(size, size))

for (r, c) in random.sample([(i, j) for i in range(size) for j in range(size)], max_twos):
    matrixreal[r][c] = 2

#for i in matrixreal:
#    print(*i)

# 1 = safe, 2 = bomb

first_row = [(0)] + [chr(65 + i) for i in range(0, size)]

matrixshown = [first_row]

for i in range(1, size):
    row = [i] + [("-") for j in range(size)]
    matrixshown.append(row)

print("\nThe board is")
for i in matrixshown:
    print(*i)

# Game loop
while True:
    rowposition = int(input("\nEnter the row number: "))
    columnposition = input("Enter the column letter: ").upper()

    while True:
        if columnposition in first_row:
            columnposition = first_row.index(columnposition)
            break
        else:
            columnposition = input("Enter a valid column letter: ").upper()
        if rowposition in range(1, size + 1):
            break
        else:
            rowposition = int(input("Enter a valid row number: "))

    if matrixreal[rowposition - 1][columnposition - 1] == 2:
        print("You hit a bomb! Game Over.")
        break
    else:
        matrixshown[rowposition][columnposition] = 1
        print("\nThe board is")
        for i in matrixshown:
            print(*i)