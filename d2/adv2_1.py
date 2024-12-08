input = """
"""

lines = list(line.split() for line in input.strip().split("\n"))
safe = 0

for line in lines:
    for j in range(len(line)):
        isSafe = True
        newLine = line[:j] + line[j+1:]
        asc = int(newLine[1]) > int(newLine[0])
        for i in range(1, len(newLine)):
            curr, prev = int(newLine[i]), int(newLine[i-1])
            diff = abs(curr - prev)
            if diff == 0 or diff > 3 or (asc and curr < prev) or (not asc and curr > prev):
                isSafe = False
                break


        if isSafe:
            safe += 1
            break

print(safe)
