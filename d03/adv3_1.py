import re

input = open("./adv3_1input.txt").read()

#Extract numbers that will be used to multiply
muls = re.findall(r'mul\(([0-9]{1,3},[0-9]{1,3})\)', input) 

result = 0

for pair in muls:
    a, b = pair.split(",")
    result += int(a) * int(b)

print(result)
