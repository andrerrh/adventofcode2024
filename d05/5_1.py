from collections import defaultdict

input = open("./input.txt").read().strip().split("\n\n")
rules = input[0].split("\n")
prints = input[1].split("\n")

graph = defaultdict(list)

for rule in rules:
    a, b = rule.split("|")
    graph[a].append(b)

validPrints = []
for prt in prints:
    vals = prt.split(",")
    valid = True
    for i in range(len(vals)):
        for j in range(i-1,-1,-1):
            if vals[i] in graph and vals[j] in graph[vals[i]]:
                valid = False
    if valid:
        validPrints.append(vals)

ans = 0
for valid in validPrints:
    ans += int(valid[len(valid)//2])

print(ans)
