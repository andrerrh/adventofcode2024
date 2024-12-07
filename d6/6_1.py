input = open("./input.txt").read().strip()

grid = input.split("\n")
m, n = len(grid), len(grid[0])

visited = set()
dirs = [[-1, 0], [0, 1], [1, 0], [0,-1]]

def helper(r, c, dirIdx):
    while True:
        visited.add((r, c))
        x, y = dirs[dirIdx]
        nr, nc = r + x, c + y
        if nr < 0 or nr >= m or nc < 0 or nc >= n:
            break

        if grid[nr][nc] == "#":
            dirIdx = (dirIdx + 1) % 4
            x, y = dirs[dirIdx]
            nr, nc = r + x, c + y

        r, c = nr, nc


for r in range(m):
    for c in range(n):
        if grid[r][c] == "^":
            helper(r, c, 0)
            break

print(len(visited))
