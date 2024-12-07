input = open("./test.txt").read().strip()

grid = input.split("\n")
m, n = len(grid), len(grid[0])
grid = [list(row) for row in grid]

visited = set()
obstacles = set()
start = set()
dirs = [[-1, 0], [0, 1], [1, 0], [0,-1]]

def helper(r, c, dirIdx, obs, newpathobs):
    while True:
        if (r,c,dirIdx) in visited or (r,c,dirIdx) in newpathobs:
            return True
        if not obs:
            visited.add((r, c, dirIdx))
        else:
            newpathobs.add((r, c, dirIdx))

        x, y = dirs[dirIdx]
        nr, nc = r + x, c + y

        if nr < 0 or nr >= m or nc < 0 or nc >= n:
            return False

        #Rotate 90 degrees else try to add obstacle
        if grid[nr][nc] == "#":
            dirIdx = (dirIdx + 1) % 4
            continue
        elif (nr, nc) not in start and (nr, nc) not in obstacles and not obs:
            grid[nr][nc] = "#"
            newset = set()
            if helper(r, c, (dirIdx + 1) % 4, 1, newset):
                obstacles.add((nr, nc))
            grid[nr][nc] = "."

        r, c = nr, nc

for r in range(m):
    for c in range(n):
        if grid[r][c] == "^":
            start.add((r,c))
            helper(r, c, 0, 0, set())
            break

print(obstacles)
print(len(obstacles))
