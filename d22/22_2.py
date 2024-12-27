from collections import deque, defaultdict

secrets = list(map(int, open("./input.txt").read().strip().splitlines()))
MOD = 16777216

sum = 0
prices = defaultdict(lambda: defaultdict(int))

for j, secret in enumerate(secrets):
    q = deque([])
    lastNum = None
    for i in range(2001):
        digit = secret % 10
        if lastNum == None:
            lastNum = digit
        else:
            q.append(digit - lastNum)
            lastNum = digit
            if len(q) > 4:
                q.popleft()
            if len(q) == 4:
                if not prices[tuple(q)][j]:
                    prices[tuple(q)][j] = digit

        secret ^= secret * 64
        secret %= MOD

        secret ^= secret // 32
        secret %= MOD

        secret ^= secret * 2048
        secret %= MOD

    sum += secret

ans = 0


for monkey in prices:
    curr = 0
    for val in prices[monkey]:
        curr += prices[monkey][val]

    ans = max(ans, curr)

print(ans)
