import re

input = open('./adv3_1input.txt').read()

mulPattern = r'mul\(([0-9]{1,3},[0-9]{1,3})\)'
doPattern = r'do\(\)'
dontPattern = r'don\'t\(\)'

muls = list(re.finditer(mulPattern, input))
dos = list(re.finditer(doPattern, input))
donts = list(re.finditer(dontPattern, input))
doIndex = 0
dontIndex = 0

i = 0
ans = 0
print(muls)
print(dos)
print(donts)

while i < len(muls):
    end = muls[i].end()
    match = muls[i].group(1)
    if end < dos[doIndex].end():
        i += 1
        continue
    elif (dos[doIndex].end() < end and dontIndex == len(donts)) or dos[doIndex].end() < end < donts[dontIndex].end():
        nums = match.split(',')
        ans += int(nums[0]) * int(nums[1])
        i += 1
    else:
        while doIndex < len(dos) and dontIndex < len(donts) and dos[doIndex].end() < donts[dontIndex].end():
            doIndex += 1
        while doIndex < len(dos) and dontIndex < len(donts) and donts[dontIndex].end() < dos[doIndex].end():
            dontIndex += 1
        if doIndex == len(dos):
            break
        
print(ans)
