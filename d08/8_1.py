from collections import defaultdict

input = open("./test.txt").read().strip().splitlines()

grid = list(map(list, input))
m, n = len(grid), len(grid[0])
freqs = defaultdict(list)

def addNode(r, c):
    if r < 0 or r >= m or c < 0 or c >= n:
        return
    grid[r][c] = "#"    

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val != ".":
            freqs[val].append((i, j))

for freq in freqs:
    freqs[freq].sort(key=lambda x: (x[0], x[1]))
    for i, (r, c) in enumerate(freqs[freq]):
        for j, (nr, nc) in enumerate(freqs[freq][i+1:]):
            dx, dy = nr - r, nc - c
            addNode(nr + dx, nc + dy)
            addNode(r - dx, c - dy)

ans = 0
for row in grid:
    print(row)
    for val in row:
        if val == "#": ans += 1
            
print(ans)
