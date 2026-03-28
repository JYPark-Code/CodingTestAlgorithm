import sys
input = sys.stdin.readline

n, k = map(int, input().split())

items = []
dp = [[0] * (k+1) for _ in range(n+1)]

# print(dp)

for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

items.sort()

# print(items)

# dp[i][w]
# i개 까지 물건 고려, 무게가 w라면 얻을 수 있는 최대 가치. 결국 dp[n][k]가
for i in range(1, n+1):
    weight, value = items[i-1]
    for w in range(1, k+1):
        if w < weight:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

# print(dp)
print(dp[n][k])