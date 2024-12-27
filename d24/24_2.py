import re
import copy
from collections import defaultdict

input = open("./test2.txt").read().strip().split("\n\n")

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

gates = {
    "AND" : lambda x, y : x & y,
    "OR" : lambda x, y : x | y,
    "XOR" : lambda x, y : x ^ y
}


def getResult(todoarg, currWires):
    while True:
        found = False
        todel = None
        if not todoarg: break

        for (w1, gate, w2, i) in todoarg:
            if w1 not in currWires or w2 not in currWires: continue
            todel = (w1,gate,w2,i)
            output = todoarg[(w1,gate,w2,i)]
            currWires[output] = gates[gate](currWires[w1],currWires[w2])
            found = True
        if found:
            del todoarg[todel]
    sum = 0
    ans = 0
    for i in range(45):
        sum += currWires[f"x{i:02}"] * 2 ** i
        sum += currWires[f"y{i:02}"] * 2 ** i
        ans += currWires[f"z{i:02}"] * 2 ** i

    ans += currWires["z45"] * 2 ** 45

    return (sum, ans)

keys = list(todo.keys())

for key1 in keys:
    for key2 in keys:
        for key3 in keys:
            for key4 in keys:
                copyObj = copy.copy(todo)
                copyWires = copy.copy(wires)
                copyObj[key1] = todo[key2]
                copyObj[key2] = todo[key1]
                copyObj[key3] = todo[key4]
                copyObj[key4] = todo[key3]
                a, b = getResult(copyObj, copyWires)
                print(a, b)
