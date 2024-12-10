input = open("./test.txt").read().strip()

grid = [list(map(int, list(row))) for row in input.splitlines()]

m, n = len(grid), len(grid[0])

def hike(r, c, prev) -> int:
    if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visited or (grid[r][c] - prev) != 1:
        return 0

    visited.add((r,c))

    if grid[r][c] == 9:
        return 1

    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    res = 0
    for x, y in dirs:
        nr, nc = r + x, c + y
        res += hike(nr, nc, grid[r][c])

    return res

ans = 0
for r in range(m):
    for c in range(n):
        if grid[r][c] == 0:
            visited = set()
            curr = ans
            ans += hike(r, c, -1)

print(ans)
