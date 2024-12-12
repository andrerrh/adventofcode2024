input = open("./input.txt").read().strip()

stones = input.split(" ")

for j in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        if int(stone) == 0:
            stones[i] = "1"
            i += 1
            continue

        stoneSize = len(stone)
        if stoneSize % 2 == 0:
            firstHalf = stone[:stoneSize//2]
            secondHalf = str(int(stone[stoneSize//2:]))
            stones[i] = firstHalf
            stones.insert(i+1, secondHalf)
            i += 2
            continue
        
        stones[i] = str(int(stone) * 2024)
        i += 1
    print(j)

print(len(stones))
