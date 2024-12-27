input = """
"""


lines = input.strip().split("\n")
list1 = [int(line.split()[0]) for line in lines]
list2 = [int(line.split()[1]) for line in lines]

list1.sort()
list2.sort()

totalDiff = 0
for num1, num2 in zip(list1, list2):
    totalDiff += abs(num1 - num2)

print(totalDiff)
