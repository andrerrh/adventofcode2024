import re

input = open("./input.txt").read().strip().splitlines()

X, Y = 101, 103 #Grid Area

robots = []
minSf = float("inf")
best = None
for row in input:
    robots.append(tuple(map(int, re.findall(r"(-?\d+)", row))))

for second in range(X * Y):
    res = []
    print(second)
    for px, py, vx, vy in robots:
        res.append(((px + vx * second) % X, (py + vy * second) % Y))

    q1, q2, q3, q4 = 0, 0, 0, 0
        
    mx, my = (X-1) // 2 , (Y-1) // 2 #middle X and middle Y
    for finalX, finalY in res:
        if finalX < mx and finalY < my: q1 += 1
        if finalX > mx and finalY < my: q2 += 1
        if finalX < mx and finalY > my: q3 += 1
        if finalX > mx and finalY > my: q4 += 1

    sf = q1 * q2 * q3 * q4
    if sf < minSf:
        minSf = sf
        best = second

print(best)
