import re

input = open("./input.txt").read().strip()

grid = input.split("\n")
m, n = len(grid), len(grid[0])

ans = 0
def backtrack(r, c, curr, nextr, nextc):
    global ans
    if r < 0 or r >= m or c < 0 or c >= n:
        return

    if not re.match(rf"\b{curr}", "XMAS"):
        return

    if curr == "XMAS":
        ans += 1

    if len(curr) >= 4:
        return
    newr = r+nextr
    newc = c+nextc
    if newr < 0 or newr >= m or newc < 0 or newc >= n:
        return
    backtrack(newr, newc, curr+grid[newr][newc],nextr,nextc)


for r in range(m):
    for c in range(n):
        if grid[r][c] == "X": 
            for nextr in range(-1, 2):
                for nextc in range(-1, 2):
                    if nextr == 0 and nextc == 0:
                        continue
                    else:
                        backtrack(r, c, grid[r][c], nextr, nextc)

print(ans)
