input = open("./input.txt").read().strip()

stones = [int(s) for s in input.split()]

cache = {}
def countStones(stone, steps):
    if (stone, steps) in cache:
        return cache[(stone, steps)]
    if steps == 0:
        return 1
    if stone == 0:
        res = countStones(1, steps - 1)
        cache[(stone, steps)] = res
        return res
    stoneString = str(stone)
    stoneSize = len(stoneString)
    if stoneSize % 2 == 0:
        firstHalf = int(stoneString[:stoneSize//2])
        secondHalf = int(stoneString[stoneSize//2:])
        res = countStones(firstHalf, steps - 1) + countStones(secondHalf, steps - 1)
        cache[(stone, steps)] = res
        return res

    else:
        res = countStones(stone * 2024, steps - 1)
        cache[(stone, steps)] = res
        return res

ans = 0
for stone in stones:
    ans += countStones(stone, 75)

print(ans)
