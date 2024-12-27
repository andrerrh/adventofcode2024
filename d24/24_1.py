import re
from collections import defaultdict

input = open("./input.txt").read().strip().split("\n\n")

initialWire = input[0].splitlines()
initialGates = input[1].splitlines()
wires = defaultdict(int)
todo = defaultdict(str)

for curr in initialWire:
    wire, val = curr.split(": ")
    wires[wire] = int(val)

for i, curr in enumerate(initialGates):
    match = re.findall(r"(\w+)", curr)
    todo[(match[0], match[1], match[2], i)] = match[3]

AND = lambda x, y : 1 if x and y else 0
OR = lambda x, y : 1 if x or y else 0
XOR = lambda x, y : 1 if x != y else 0

gates = {
    "AND": AND,
    "OR": OR,
    "XOR": XOR,
}

while True:
    found = False
    todel = None
    if not todo: break

    for (w1, gate, w2, i) in todo:
        if w1 not in wires or w2 not in wires: continue
        todel = (w1,gate,w2,i)
        output = todo[(w1,gate,w2,i)]
        wires[output] = gates[gate](wires[w1],wires[w2])
        found = True
    if found:
        del todo[todel]

ans = 0
for i in range(46):
    ans += wires[f"z{i:2}"] * 2 ** i

print(ans)
