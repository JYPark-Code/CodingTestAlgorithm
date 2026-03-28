import sys
input = sys.stdin.readline
n,m = map(int, input().split())

INF = float('inf')

rock_map = [True] * (n + 1)
max_jump = int((2 * n) ** 0.5) + 2
# dp[위치][마지막 점프 길이] 로 두어서 생각하자.
dp = [[INF] * (max_jump + 1) for _ in range(n + 1)]


for _ in range(m):
    idx = int(input().strip())
    rock_map[idx] = False

dp[1][0] = 0

# 최대 점프 가능 & 못 가는 위치 & 남은 거리 고려
for i in range(2, n+1):
    for j in range(1, max_jump+1):
        if not rock_map[i]:
            continue

        prev = i-j
        if prev < 1:
            break

        candidates = []

        for prev_jump in (j - 1, j, j + 1):
            # 범위 체크 & 도달 가능 체크
            if 0 <= prev_jump <= max_jump and dp[prev][prev_jump] != INF:
                # 가능하면 candidates에 추가
                candidates.append(dp[prev][prev_jump])
        if candidates:
            dp[i][j] = min(candidates) + 1

if min(dp[n]) == INF:
    print(-1)
    exit()

print(min(dp[n]))