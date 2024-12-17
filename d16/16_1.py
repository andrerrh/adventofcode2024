import heapq

input = open("./input.txt").read().strip().splitlines()

grid = [list(row) for row in input]
m, n = len(grid), len(grid[0])

start, end = [0,0], [0,0]

for r in range(m):
    for c in range(n):
        if grid[r][c] == "S": start = [r,c]

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
currMin = float("inf")
pq = [(0, start[0], start[1], 0)]

bestPath = 10**9+7

while pq:
    s, r, c, d = heapq.heappop(pq) #Score, Row, Column, Direction

    if s > bestPath: break

    if grid[r][c] == "E":
        print(s)
        bestPath = s
        continue
    
    for i, (x, y) in enumerate(dirs):
        nr, nc = r + x, c + y
        if grid[nr][nc] != "#":
            if d == i:
                heapq.heappush(pq, (s+1,nr,nc,i))
            elif (d+1)%4 == i or (d-1)%4 == i:
                heapq.heappush(pq, (s+1001,nr,nc,i))
            else:
                continue
