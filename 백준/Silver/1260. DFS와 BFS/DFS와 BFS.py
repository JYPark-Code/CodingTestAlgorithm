import sys
input = sys.stdin.readline
from collections import deque

# 정점, 간선, 탐색 시작
n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)

# dfs
def dfs(dfs_graph, dfs_start):

    dfs_visited[dfs_start] = True
    print(dfs_start, end=" ")
    
    for next_node in dfs_graph[dfs_start]:
        if not dfs_visited[next_node]:
            dfs(dfs_graph, next_node)

# bfs
def bfs(bfs_graph, bfs_start):

    bfs_visited = [False] * (n + 1)
    queue = deque([bfs_start])

    while queue:
        v = queue.popleft()

        if not (bfs_visited[v]):
            print(v, end=" ")
            bfs_visited[v] = True

        for beside_node in bfs_graph[v]:
            if not bfs_visited[beside_node]:
                queue.append(beside_node)

dfs(graph, start)
print()
bfs(graph, start)