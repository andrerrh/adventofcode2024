import re
import heapq

input = open("./input.txt").read().strip()

match = re.findall(r"\d+", input)
coords = [(int(match[i+1]), int(match[i])) for i in range(0, len(match), 2)]

gridSize = 71
bytesN = 1024
grid = [[0 for _ in range(gridSize)] for _ in range(gridSize)]

for i in range(bytesN):
    r, c = coords[i]
    grid[r][c] = 1

def isInbound(r, c):
    return r >= 0 and r < gridSize and c >= 0 and c < gridSize

while True:
    h = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))
    while h:
        moves, r, c = heapq.heappop(h)
        if r == gridSize - 1 and c == gridSize - 1:
            break
        for x, y in [[0,1], [1,0], [0,-1],[-1,0]]:
            nr, nc = r + x, c + y
            if isInbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != 1:
                visited.add((nr, nc))
                heapq.heappush(h, (moves+1, nr, nc))
    else:
        r, c = coords[bytesN-1]
        print(f"{c},{r}")
        break

    r, c = coords[bytesN]
    grid[r][c] = 1
    bytesN += 1

