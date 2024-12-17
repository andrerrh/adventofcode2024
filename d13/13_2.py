import re

input = open("./input.txt").read().strip().split("\n\n")
ba, bb, prize = [], [], []

for machine in input:
    match = re.findall(r"(\d+)", machine)
    ba.append((int(match[0]), int(match[1])))
    bb.append((int(match[2]), int(match[3])))
    prize.append((int(match[4]) + 10000000000000, int(match[5]) + 10000000000000))

tokens = 0

for i in range(len(ba)):
    ax, ay = ba[i]
    bx, by = bb[i]
    px, py = prize[i]

    sa = (px*by-py*bx) / (ax*by-ay*bx)
    sb = (px-sa*ax) / bx
    if sa % 1 == 0 and sb % 1 == 0:
        tokens += sa * 3 + sb

print(int(tokens))
