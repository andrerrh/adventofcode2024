from collections import defaultdict

input = open("./input.txt").read().strip().split("\n")

grid = [list(row) for row in input]
m, n = len(grid), len(grid[0])

visited = set()
area = defaultdict(int)
perimeter = defaultdict(list)

def isValid(r, c):
    return r >= 0 and r < m and c >= 0 and c < n

def dfs(r, c, id):
    curr = grid[r][c]
    area[id] += 1
    visited.add((r,c))
    for i, (x, y) in enumerate([[0, 1], [1, 0], [0, -1], [-1, 0]]):
        nr, nc = r + x, c + y
        if isValid(nr, nc) and curr == grid[nr][nc]:
            if (nr, nc) not in visited:
                dfs(nr, nc, id)
        else:
            perimeter[id].append(((r + nr) / 2, (c + nc) / 2, i))

id = 0
for r in range(m):
    for c in range(n):
        if (r, c) not in visited:
            dfs(r, c, id)
            id += 1

def countSides(id):
    upBorder = []
    rightBorder = []
    downBorder = []
    leftBorder = []
    for r, c, d in perimeter[id]:
        if d == 0:
            rightBorder.append((r, c))
        elif d == 1:
            downBorder.append((r, c))
        elif d == 2:
            leftBorder.append((r, c))
        else:
            upBorder.append((r, c))

    upBorder.sort(key=lambda x: (x[0], x[1]))
    downBorder.sort(key=lambda x: (x[0], x[1]))
    leftBorder.sort(key=lambda x: (x[1], x[0]))
    rightBorder.sort(key=lambda x: (x[1], x[0]))
    
    sides = 0
    for i in range(1, len(upBorder)):
        if upBorder[i][0] != upBorder[i-1][0] or upBorder[i][1] - upBorder[i-1][1] != 1:
            sides += 1
    for i in range(1, len(downBorder)):
        if downBorder[i][0] != downBorder[i-1][0] or downBorder[i][1] - downBorder[i-1][1] != 1:
            sides += 1
    for i in range(1, len(rightBorder)):
        if rightBorder[i][1] != rightBorder[i-1][1] or rightBorder[i][0] - rightBorder[i-1][0] != 1:
            sides += 1
    for i in range(1, len(leftBorder)):
        if leftBorder[i][1] != leftBorder[i-1][1] or leftBorder[i][0] - leftBorder[i-1][0] != 1:
            sides += 1
    sides += 4

    return sides

ans = 0
for id in area:
    ans += area[id] * countSides(id)

print(ans)
