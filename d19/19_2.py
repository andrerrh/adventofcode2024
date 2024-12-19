from functools import cache

input = open("./input.txt").read().strip().split("\n\n")

patterns = set(input[0].split(", "))
designs = input[1].splitlines()

@cache
def backtrack(word):
    if word == "":
        return 1

    count = 0

    for i in range(len(word) + 1):
        if word[:i] in patterns:
            possibilities = backtrack(word[i:])
            count += possibilities
    return count


count = 0
for d in designs:
    count += backtrack(d)
print(count)

