import sys
input = sys.stdin.readline

# DP 테이블이 좀 더 맞는 문제
MAX = float('inf')

n, k = map(int, input().split())

coins = []
dp = [MAX] * (k + 1)
dp[0] = 0

for _ in range(n):
    coins.append(int(input().strip()))

for i in range(k + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == MAX:
    print(-1)
else:
    print(dp[k])