#Only valid for my input of the problem
import re

program = list(map(int, re.findall(r"\d+", open("./input.txt").read())))
program = program[3:]

print(program)

def checkNums(program, curr):

    if not program:
        return curr

    for i in range(8):
        a = (curr << 3) + i
        b = i ^ 1
        c = a >> b
        b = b ^ 4
        b = b ^ c
    
        if b % 8 == program[-1]: #if true, valid possible value for the answer
            next = checkNums(program[:-1], a)
            if next is None: continue
            return next

print(checkNums(program, 0))

# b = a % 8
# b = b ^ 1
# c = a >> b
# a = a >> 3
# b = b % 4
# b = b ^ c
# out = b % 8
# jmp if a == 0
