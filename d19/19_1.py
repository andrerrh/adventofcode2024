from functools import cache

input = open("./input.txt").read().strip().split("\n\n")

patterns = set(input[0].split(", "))
designs = input[1].splitlines()

@cache
def backtrack(word):
    if word == "":
        return True

    for i in range(len(word) + 1):
        if word[:i] in patterns and backtrack(word[i:]):
            return True
    return False

ans = 0
for d in designs:
    ans += 1 if backtrack(d) else 0
print(ans)
