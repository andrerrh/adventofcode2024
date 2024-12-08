from collections import defaultdict

input = """
"""

lines = input.strip().split("\n")
list1 = [int(line.split()[0]) for line in lines]
list2 = [int(line.split()[1]) for line in lines]

freq = defaultdict(int)

for num in list2:
    freq[num] += 1

total = 0

for num in list1:
    if num in freq:
        total += num * freq[num]

print(total)

