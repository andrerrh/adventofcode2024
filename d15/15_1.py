input = open("./input.txt").read().strip().split("\n\n")

grid = [list(row) for row in input[0].split("\n")]
moves = ''.join(input[1])

m, n = len(grid), len(grid[0])

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
robot = []

def moveIfEmpty(r, c, nr, nc, curr):
    if grid[nr][nc] == ".":
        grid[nr][nc] = curr
        grid[r][c] = "."
        return True
    return False

def move(r, c, dirIndex, curr):
    global robot
    x, y = dirs[dirIndex]
    nr, nc = r + x, c + y

    if grid[nr][nc] == "#":
        return
    elif grid[nr][nc] == "O":
        move(nr, nc, dirIndex, "O")
    if curr == "O":
        moveIfEmpty(r, c, nr, nc, curr)
        return

    if curr == "@":
        if moveIfEmpty(r, c, nr, nc, curr):
            robot = [nr, nc]

for r in range(m):
    for c in range(n):
        if grid[r][c] == "@":
            robot = [r,c]

for char in moves:
    dir = -1
    if char == ">": dir = 0
    if char == "v": dir = 1
    if char == "<": dir = 2
    if char == "^": dir = 3
    if dir == -1: continue

    move(robot[0], robot[1], dir, "@")

ans = 0
for r in range(m):
    for c in range(n):
        if grid[r][c] == "O":
            ans += 100 * r + c

print(ans)
