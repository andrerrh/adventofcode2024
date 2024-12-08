from itertools import product

input = open("./input.txt").read().strip().split("\n")

results = []
numsList = []

for el in input:
    equation = el.split(":")
    results.append(int(equation[0]))
    numsList.append(list(map(int, equation[1].strip().split(" "))))

ans = 0
def findOperations(result, vals):
    global ans
    operations = list(product(['+','*', '||'], repeat=len(vals) - 1))
    
    for ops in operations:
        res = vals[0]
        for i in range(1, len(vals)):
            if ops[i-1] == "+":
                res += vals[i]
            if ops[i-1] == "*":
                res *= vals[i]
            if ops[i-1] == "||":
                length = len(str(vals[i]))
                res *= 10 ** length
                res += vals[i]

        if res == result:
            ans += res
            break

for i in range(len(results)):
    findOperations(results[i], numsList[i])

print(ans)

