from collections import deque, defaultdict
from itertools import product
from functools import cache

input = open("./input.txt").read().strip().splitlines()

numpad = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"]
]


robotpad = [
    [None,"^","A"],
    ["<","V",">"]
]

numPossibilities = defaultdict(list)
robotPossibilities = defaultdict(list)

def findPossibles(sr,sc,tr,tc,pad):
    q = deque([(sr,sc,"")])
    possibles = []
    seen = set()
    maxPoss = float("inf")
    while q:
        r, c, acc = q.popleft()

        seen.add((r,c))

        if r == tr and c == tc:
            if len(acc) > maxPoss: continue
            maxPoss = len(acc)
            possibles.append(acc + "A")

        for nr, nc, dir in [[r,c+1,">"],[r+1,c,"V"],[r,c-1,"<"],[r-1,c,"^"]]:
            if nr < 0 or nc < 0 or nr >= len(pad) or nc >= len(pad[0]): continue
            if pad[nr][nc] == None: continue
            if (nr, nc) in seen: continue
            q.append((nr,nc,acc+dir))

    return possibles

for pad in [numpad, robotpad]:
    for sr in range(len(pad)):
        for sc in range(len(pad[0])):
            if pad[sr][sc] == None: continue
            for tr in range(len(pad)):
                for tc in range(len(pad[0])):
                    if pad[tr][tc] == None: continue
                    if pad[sr][sc] != pad[tr][tc]:
                        possibles = findPossibles(sr,sc,tr,tc,pad)
                    else:
                        possibles = ["A"]
                    if possibles:
                        if pad == numpad:
                            numPossibilities[(pad[sr][sc],pad[tr][tc])] = possibles
                        else:
                            robotPossibilities[(pad[sr][sc],pad[tr][tc])] = possibles

robotLens = {key: len(value[0]) for key, value in robotPossibilities.items()}

@cache
def calculate(s, t, depth):
    if depth == 1:
        return robotLens[(s,t)]
    optimal = float("inf")
    for path in robotPossibilities[(s,t)]:
        dist = 0
        for x, y in zip("A" + path, path):
            dist += calculate(x,y,depth-1)
        optimal = min(optimal, dist)
    return optimal

ans = 0
for code in input:
    initial = [(numPossibilities[(s,t)]) for s,t in zip("A" + code, code)] 
    r1 = list("".join(x) for x in product(*initial))
    optimal = float("inf")
    for path in r1:
        dist = 0
        for x, y in zip("A" + path, path):
            dist += calculate(x,y,25)
        optimal = min(optimal, dist)
    ans += optimal * int(code[:3])
print(ans)
