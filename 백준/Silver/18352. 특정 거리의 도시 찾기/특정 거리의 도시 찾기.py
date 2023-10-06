from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, dest = map(int, input().split())
    graph[start].append(dest)

# 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# BFS 수행
q = deque([x])

while q:
    now = q.popleft()
    # 모든 도시 확인
    for next_node in graph[now]:
        # 아직 미방문 시
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리 K 오름차순으로 출력:
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)