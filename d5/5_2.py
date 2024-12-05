from collections import defaultdict

input = open("./input.txt").read().strip().split("\n\n")
rules = input[0].split("\n")
prints = input[1].split("\n")

graph = defaultdict(list)

for rule in rules:
    a, b = rule.split("|")
    graph[a].append(b)

invalidPrints = []
for prt in prints:
    vals = prt.split(",")
    valid = True
    for i in range(len(vals)):
        for j in range(i-1,-1,-1):
            if vals[i] in graph and vals[j] in graph[vals[i]]:
                valid = False
    if not valid:
        invalidPrints.append(vals)

transformed = [] #prints after valid transformation
for prt in invalidPrints:
    newPrint = [prt[0]]
    for i in range(1, len(prt)):
        inserted = False
        for j in range(len(newPrint)):
            if prt[i] in graph and newPrint[j] in graph[prt[i]]:
                newPrint.insert(j, prt[i])
                inserted = True
                break
        if not inserted:
            newPrint.append(prt[i])
    transformed.append(newPrint)

ans = 0
for prt in transformed:
    ans += int(prt[len(prt) // 2])

print(ans)
