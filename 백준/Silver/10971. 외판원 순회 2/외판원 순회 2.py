import sys
import math
input = sys.stdin.readline

N = int(input())
W = list()
visited = [False] * N
for _ in range(N):
    W.append(list(map(int, input().split())))

start = 0

# answer = float('inf') # float형이 아니라 inf(무한대)를 나타내기 위해서...
answer = math.inf

def dfs(now, count, cost):
    global answer # global 안하면 읽을 순 있지만 값 수정이 안된다.

    if cost >= answer:
        return

    # 마지막 도시에 도달했을 때
    if count == N:
        if W[now][start] != 0:
            answer = min(answer, cost + W[now][start])
        return

    # 도시 방문
    for i in range(N):

        if not visited[i] and W[now][i] != 0:

            visited[i] = True
            dfs(i, count + 1, cost + W[now][i])
            visited[i] = False

visited[start] = True
dfs(start, 1, 0)

print(answer)