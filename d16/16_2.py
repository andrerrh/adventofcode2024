from collections import deque
import heapq

input = open("./input.txt").read().strip().splitlines()

grid = [list(row) for row in input]
m, n = len(grid), len(grid[0])

start, end = [0,0], [0,0]

for r in range(m):
    for c in range(n):
        if grid[r][c] == "S": start = [r,c]

pq = [(0, start[0], start[1], 0, 1)]
lowestCost = {(start[0], start[1], 0, 1): 0}
backtrack = {}
bestCost = float("inf")
endStates = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    if cost > lowestCost.get((r, c, dr, dc), float("inf")): continue
    if grid[r][c] == "E":
        if cost > bestCost: break
        bestCost = cost
        endStates.add((r, c, dr, dc))
    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
        if grid[nr][nc] == "#": continue
        lowest = lowestCost.get((nr, nc, ndr, ndc), float("inf"))
        if new_cost > lowest: continue
        if new_cost < lowest:
            backtrack[(nr, nc, ndr, ndc)] = set()
            lowestCost[(nr, nc, ndr, ndc)] = new_cost
        backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

states = deque(endStates)
seen = set(endStates)

while states:
    key = states.popleft()
    for last in backtrack.get(key, []):
        if last in seen: continue
        seen.add(last)
        states.append(last)

print(len({(r, c) for r, c, _, _ in seen}))
