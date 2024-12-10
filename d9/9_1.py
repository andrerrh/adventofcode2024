input = open("./input.txt").read().strip()

n = len(input)
spaces = []
fileid = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(int(input[i])):
            spaces.append(f"{fileid}")
        fileid += 1
    else:
        if int(input[i]) != 0:
            for j in range(int(input[i])):
                spaces.append(".")

l, r = 0, len(spaces) - 1
while l < r:
    if spaces[l] != ".":
        l += 1
        continue
    while spaces[r] == ".":
        r -= 1

    spaces[l] = spaces[r]
    spaces[r] = "."
    l += 1
    r -= 1

i = 0
ans = 0
while spaces[i] != ".":
    ans += i * int(spaces[i])
    i += 1

print(len(spaces))
print(ans)
