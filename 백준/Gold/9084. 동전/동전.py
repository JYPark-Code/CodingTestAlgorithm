import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    kinds = int(input().strip())
    moneys = []
    moneys.extend(list(map(int, input().split())))
    target_money = int(input().strip())

    dp = [0] * (target_money + 1)
    prev = 0

    dp[0] = 1 # Starting point
    for money in moneys:
        for i in range(money, target_money + 1):
            dp[i] += dp[i - money]

    # print(dp)
    print(dp[-1])