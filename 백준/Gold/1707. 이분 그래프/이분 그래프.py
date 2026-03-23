import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    # 그래프의 정점 수 = v, 간선 수 = e
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    color = [-1] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    is_bipartite = True
    
    for i in range(1, v+1):
        if color[i] == -1:
            queue.append(i)
            color[i] = 0

            while queue:
                cur = queue.popleft()

                for next_node in graph[cur]:
                    if color[next_node] == -1:
                        color[next_node] = 1 - color[cur]
                        queue.append(next_node)

                    if color[cur] == color[next_node]:
                        is_bipartite = False
                        break

        if not is_bipartite:
            break

    if is_bipartite:
        print("YES")
    else:
        print("NO")