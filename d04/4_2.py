from collections import defaultdict

input = open("./input.txt").read().strip()
grid = input.split("\n")

for i in range(len(grid)):
    row = list(grid[i])
    row.insert(0, ".")
    row.append(".")
    grid[i] = "".join(row)

n = len(grid[0])
newrow = "." * n
grid.insert(0, newrow)
grid.append(newrow)

m = len(grid)

ans = 0

def crossTest(r, c):
    neis = [grid[r-1][c-1],grid[r-1][c+1],grid[r+1][c-1],grid[r+1][c+1]]
    count = defaultdict(int)
    for val in neis:
        count[val] += 1

    if count["M"] == 2 and count["S"] == 2 and grid[r-1][c-1] != grid[r+1][c+1]:
        return True
    return False



for r in range(m):
    for c in range(n):
        char = grid[r][c]
        if char == "A":
            if crossTest(r, c):
                ans += 1

print(ans)


