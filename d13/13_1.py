import re
import math

input = open("./test.txt").read().strip().split("\n\n")

ba = [] #3 to push button a
bb = [] #1 to push button b
prize = []
for machine in input:
    match = re.findall(r"(\d+)", machine)
    ba.append((int(match[0]), int(match[1])))
    bb.append((int(match[2]), int(match[3])))
    prize.append((int(match[4]), int(match[5])))

tokens = 0

for i in range(len(ba)):
    ax, ay = ba[i]
    bx, by = bb[i]
    px, py = prize[i][0], prize[i][1]
    
    currA, currB = 0, max(math.ceil(px/bx), math.ceil(py/by))
    currX, currY = currB * bx, currB * by
    
    while currX > px or currY > py:
        currX -= bx
        currY -= by
        currB -= 1

        while currX < px or currY < py:
            currX += ax
            currY += ay
            currA += 1

        if (
            currB < 0 or
            currA < 0 or
            currX < 0 or
            currY < 0
        ):
            break

        if currX == px and currY == py and currB <= 100:
            tokens += currA * 3 + currB


print(tokens)
