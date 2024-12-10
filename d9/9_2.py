input = open("./input.txt").read().strip()

n = len(input)
spaces = []
fileid = 0

for i in range(n):
    if i % 2 == 0:
        spaces.append([fileid] * int(input[i])) #Value, Have been shifted
        fileid += 1
    else:
        if int(input[i]) != 0:
            spaces.append(["."] * int(input[i]))

r = len(spaces) - 1
while r >= 0:
    l = 0
    if "." in spaces[r]:
        r -= 1
        continue

    while len(spaces[l]) < len(spaces[r]) or "." not in spaces[l]:
        l += 1
        if l >= r:
            break
    
    if l >= r:
        r -= 1
        continue

    if len(spaces[l]) >= len(spaces[r]):
        leftover = len(spaces[l]) - len(spaces[r])
        spaces[l] = spaces[r].copy()
        spaces[r] = ["."] * len(spaces[r])
        if leftover != 0:
            spaces.insert(l+1, ["."] * leftover)
            r += 1
    r -= 1

finalCode = []
for i in range(len(spaces)):
    val = spaces[i]
    for i in range(len(val)):
        finalCode.append(val[i])

ans = 0
for i in range(len(finalCode)):
    if finalCode[i] != ".":
        ans += int(finalCode[i]) * i

print(ans)
