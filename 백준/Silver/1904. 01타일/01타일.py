import sys
input = sys.stdin.readline
# 00 또는 1 하나 있음
N = int(input().strip())

dp = [0] * (N + 2)

dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])