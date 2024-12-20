from collections import deque
import copy

input = open("./input.txt").read().strip().splitlines()
grid = [list(row) for row in input]
m, n = len(grid) , len(grid[0])


sr,sc,er,ec = 0,0,0,0
for r in range(m):
    for c in range(n):
        val = grid[r][c]
        if val == "S": sr, sc = r, c
        if val == "E": er, ec = r, c

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
q = deque([(er, ec, 0)])#r,c,moves,cheat time
visited = set()
altGrid = copy.deepcopy(grid)

while q:
    r, c, moves = q.popleft()

    visited.add((r, c))
    altGrid[r][c] = moves
    if r == sr and c == sc:
        maxM = moves
        break

    for x, y in dirs:
        nr, nc = r + x, c + y
        if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
        if grid[nr][nc] == '#': continue
        if (nr,nc) in visited: continue
        q.append((nr,nc, moves + 1))

limit = 100
skips = 0
for r, c in visited:
    if r == er and c == ec: continue
    curr = int(altGrid[r][c])
    
    for rad in range(2, 21):
        for dr in range(rad + 1):
            dc = rad - dr
            for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                if nr < 0 or nc < 0 or nr >= m or nc >= n: continue
                if altGrid[nr][nc] == "#": continue
                if curr - altGrid[nr][nc] >= limit + rad: skips += 1

print(skips)

