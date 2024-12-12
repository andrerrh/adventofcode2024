from collections import defaultdict

input = open("./input.txt").read().strip().split("\n")

grid = [list(row) for row in input]
m, n = len(grid), len(grid[0])

visited = set()
area = defaultdict(int)
perimeter = defaultdict(int)

def isValid(r, c):
    return r >= 0 and r < m and c >= 0 and c < n

def dfs(r, c, id):
    curr = grid[r][c]
    area[f"{curr}{id}"] += 1
    visited.add((r,c))
    for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nr, nc = r + x, c + y
        if isValid(nr, nc) and curr == grid[nr][nc]:
            if (nr, nc) not in visited:
                dfs(nr, nc, id)
        else:
            perimeter[f"{curr}{id}"] += 1

id = 0
for r in range(m):
    for c in range(n):
        if (r, c) not in visited:
            dfs(r, c, id)
            id += 1
ans = 0
for key in area:
    ans += area[key] * perimeter[key]

print(ans)
