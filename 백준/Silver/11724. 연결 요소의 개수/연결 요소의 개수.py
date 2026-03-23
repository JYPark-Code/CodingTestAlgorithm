import sys
input = sys.stdin.readline
from collections import deque

# n : 정점 개수, m : 간선 개수
n , m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = set()

count = 0

# 그래프 채우기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def bfs(graph_, start):
    queue = deque([start])
    bfs_visited = set()

    while queue:
        v = queue.popleft()

        for i in graph_[v]:
            if i not in bfs_visited:
                queue.append(i)
                bfs_visited.add(i)

    return bfs_visited

for i in range(1, n + 1):

    if i in visited:
        continue

    visited_set = bfs(graph, i)
    visited.update(visited_set)
    count += 1

    if len(visited_set) == n:
        break

print(count)