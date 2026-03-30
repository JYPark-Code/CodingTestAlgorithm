import sys
input = sys.stdin.readline

T = int(input().strip())
INF = float('inf')

W = [[] for _ in range(T)]

for i in range(T):
    W[i].extend(map(int, input().split()))

"""
1 << T = 1을 몇번 밀었다. = 2**T와 동일하게 나옴
x << T = x * (2 ** T) 이다. 일단 비트마스크 문제라 저걸 한번 써보는 것도 나쁘지 않음.
-1 이 총 2^4 = 16개가 나올것이다.
dp[now][visited] : 현재 now에 있고, visited 상태일 때 남은 도시를 다 돌고 시작점으로 돌아가는 최소 비용
비트 마스크로 0000 : 방문한 곳 X, 0001 한 곳만 방문함. 1111 모두 방문함
"""
dp = [[-1] * (1 << T) for _ in range(T)]


## visited & (1 << next) <- 방문했는가?

# 1. dfs로 모든 곳 방문 체크
def dfs(now, visited):
    # 1. 종료 조건 (base case) - 모든 도시를 방문했는가?
    if visited == (1 << T) - 1:
        if W[now][0] == 0:
            return INF
        return W[now][0]

    # 2. dp 체크
    if dp[now][visited] != -1:
        return dp[now][visited]
    # 3. result 초기화
    result = INF

    # 4. for next in ...
    for next in range(T):
        # 5. 조건 검사 (방문했는지?)
        if W[now][next] == 0 or visited & (1 << next):
            continue

        # 6. 최소값 갱신
        result = min(result, W[now][next] + dfs(next, visited | (1 << next)))

    # 7. dp 저장
    dp[now][visited] = result

    return result

print(dfs(0, 1 << 0))