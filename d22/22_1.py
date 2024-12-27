secrets = list(map(int, open("./input.txt").read().strip().splitlines()))
MOD = 16777216

sum = 0
for secret in secrets:
    for _ in range(2000):
        secret ^= secret * 64
        secret %= MOD

        secret ^= secret // 32
        secret %= MOD

        secret ^= secret * 2048
        secret %= MOD
    sum += secret
print(sum)
