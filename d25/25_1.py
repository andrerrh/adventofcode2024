input = [grid.splitlines() for grid in (open("./input.txt").read().strip().split("\n\n"))]

locks = []
keys = []

for grid in input:
    curr = [0] * 5
    if grid[0][0] == "#":
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr[j] += 1 if grid[i][j] == "#" else 0
        locks.append(curr)
    else:
        if grid[0][0] == ".":
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    curr[j] += 1 if grid[i][j] == "#" else 0
            keys.append(curr)

ans = 0
for lock in locks:
    for key in keys:
        for i in range(5):
            if lock[i] + key[i] > 7: break
        else:
            ans += 1

print(ans)
