import re

input = open("./input.txt").read().strip()

match = re.findall(r"(\d+)", input)

combo = [
    0,
    1,
    2,
    3,
    int(match[0]),
    int(match[1]),
    int(match[2])
]
program = []
output = []
pointer = 0


def updatePointer(step):
    global pointer
    pointer += step

def adv(operand):
    combo[4] = combo[4] >> combo[operand]
    updatePointer(2)

def bxl(operand):
    combo[5] ^= operand
    updatePointer(2)

def bst(operand):
    combo[5] = combo[operand] % 8
    updatePointer(2)

def jnz(operand):
    global pointer
    if combo[4] != 0:
        pointer = operand
    else:
        updatePointer(2)

def bxc(operand):
    combo[5] ^= combo[6]
    updatePointer(2)

def out(operand):
    output.append(combo[operand] % 8)
    updatePointer(2)

def bdv(operand):
    combo[5] = combo[4] >> combo[operand]
    updatePointer(2)

def cdv(operand):
    combo[6] = combo[4] >> combo[operand]
    updatePointer(2)

op = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

for i in range(3, len(match)):
    program.append(int(match[i]))

while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer+1]
    op[opcode](operand)

print(",".join(map(str, output)))
