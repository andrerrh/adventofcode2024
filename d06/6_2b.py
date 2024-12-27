input = open("./input.txt").read().strip()

grid = input.split("\n")
m, n = len(grid), len(grid[0])
grid = [list(row) for row in grid]

visited = set()
dirs = [[-1, 0], [0, 1], [1, 0], [0,-1]]

def isOutside(r,c):
    return r < 0 or r >= m or c < 0 or c >= n

def walk(r, c, dirIdx, grid, path):
    while True:
        if (r,c,dirIdx) in path:
            return True

        path.add((r,c,dirIdx))
        x, y = dirs[dirIdx]
        nr, nc = r + x, c + y

        if isOutside(nr, nc):
            return False

        if grid[nr][nc] == "#":
            dirIdx = (dirIdx + 1) % 4
            continue

        r, c = nr, nc

initialPath = set()
start = {}

for r in range(m):
    for c in range(n):
        if grid[r][c] == "^":
            start[0] = [r,c]
            break

walk(start[0][0], start[0][1], 0, grid, initialPath)

ans = 0
obstacles = set()
for r, c, dirIdx in initialPath:
    x, y = dirs[dirIdx]
    nr, nc = r + x, c + y

    if (
        (nr, nc) in obstacles or
        isOutside(nr, nc) or
        grid[nr][nc] == "#" or
        (nr == start[0][0] and nc == start[0][1])
    ):
        continue

    grid[nr][nc] = "#"
    newset = set()
    if walk(start[0][0], start[0][1], 0, grid, newset):
        obstacles.add((nr,nc))
    grid[nr][nc] = "."

print(len(obstacles))
