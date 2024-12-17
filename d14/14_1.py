import re

input = open("./input.txt").read().strip().splitlines()

T = 100 #Iterations
X, Y = 101, 103 #Grid Area

q1, q2, q3, q4 = 0, 0, 0, 0
ans = 0

for row in input:
    px, py, vx, vy = list(map(int, re.findall(r"(-?\d+)", row)))
 
    moveX, moveY = vx * T, vy * T
    finalX, finalY = (moveX + px) % X, (moveY + py) % Y

    if finalX < 0: finalX = X - finalX
    if finalY < 0: finalY = Y - finalY
    
    mx, my = (X-1) / 2 , (Y-1) / 2 #middle X and middle Y
    if finalX < mx and finalY < my: q1 += 1
    if finalX > mx and finalY < my: q2 += 1
    if finalX < mx and finalY > my: q3 += 1
    if finalX > mx and finalY > my: q4 += 1

ans = q1 * q2 * q3 * q4
print(q1,q2,q3,q4)
print(ans)
