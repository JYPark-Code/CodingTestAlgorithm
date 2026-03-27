import sys
input = sys.stdin.readline

n, k = map(int, input().split())

money_kind = []

for _ in range(n):
    money_kind.append(int(input().strip()))

money_kind.sort(reverse=True)
# print(money_kind)

count = 0

for money in money_kind:
    if k >= money:
        money_count = k // money
        count += money_count
        k %= money

    if k == 0:
        break

print(count)