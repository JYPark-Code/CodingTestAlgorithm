import sys
input = sys.stdin.readline
from collections import deque

n = int(input().strip())
m = int(input().strip())

graph = [[] for x in range(n + 1)] # 이동 경로 그래프
indegree = [0] * (n + 1) # 차수
dist = [0] * (n + 1) # 가장 오래 걸리는 시간
parent = [[] for x in range(n + 1)] # 가장 오래 걸리는 시간 직전에 방문한 노드

for _ in range(m):
    start, destination, time_takes = map(int, input().split())
    graph[start].append((destination, time_takes))
    indegree[destination] += 1

han, rome = map(int, input().split())

# print("graph : ", graph)
# print("indegree : ", indegree)

queue = deque([han])

while queue:
    v = queue.popleft()

    for next_road in graph[v]:
        dest, times = next_road

        # 시간 걸릴 후보
        candidate = dist[v] + times

        if candidate > dist[dest]:
            dist[dest] = candidate
            parent[dest] = [v]

        elif candidate == dist[dest]:
            parent[dest].append(v)

        indegree[dest] -= 1

        if indegree[dest] == 0:
            queue.append(dest)

# print(parent)
print(dist[rome]) # 가장 오래 걸린 시간

# 다시 로마부터 역방향으로 카운트 하기
rome_queue = deque([rome])
visited = {rome}
count = 0

while rome_queue:
    current = rome_queue.popleft()

    for prev in parent[current]:
        count += 1
        if prev not in visited:
            visited.add(prev)
            rome_queue.append(prev)

# print(visited)
print(count)
