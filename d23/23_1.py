import re
from collections import defaultdict

input = open("./input.txt").read().strip().splitlines()

graph = defaultdict(lambda: defaultdict(bool))
for row in input:
    (p1, p2) = re.findall(r"(\w+)", row)
    graph[p1][p2] = True
    graph[p2][p1] = True

sets = set()

for p1 in graph:
    for p2 in graph[p1]:
        for p3 in graph[p1]:
            if p2 == p3: continue
            if p2 in graph[p3] and ("t" == p1[0] or "t" == p2[0] or "t" == p3[0]):
                toadd = tuple(sorted([p1,p2,p3]))
                sets.add(toadd)

print(len(sets))
