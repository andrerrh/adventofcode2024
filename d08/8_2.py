from collections import defaultdict

input = open("./input.txt").read().strip().splitlines()

grid = list(map(list, input))
m, n = len(grid), len(grid[0])
freqs = defaultdict(list)

def validPos(r, c):
    return r >= 0 and r < m and c >= 0 and c < n

def addNode(r, c):
    if not validPos(r, c):
        return
    grid[r][c] = "#"    

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val != ".":
            freqs[val].append((i, j))

for freq in freqs:
    freqs[freq].sort(key=lambda x: (x[0], x[1]))
    for i, (r, c) in enumerate(freqs[freq]):
        for nr, nc in freqs[freq][i+1:]:
            dx, dy = nr - r, nc - c
            newr, newc = nr, nc
            while validPos(newr, newc):
                addNode(newr, newc)
                newr += dx
                newc += dy
            newr, newc = r, c
            while validPos(newr, newc):
                addNode(newr , newc)
                newr -= dx
                newc -= dy

ans = 0
for row in grid:
    for val in row:
        if val == "#": ans += 1
            
print(ans)

