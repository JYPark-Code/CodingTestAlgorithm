# N장의 카드 제공 M에 가까운 3장의 합 뽑기
# 배열, 완전 탐색
n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= m:
                answer = max(answer, temp)

print(answer)