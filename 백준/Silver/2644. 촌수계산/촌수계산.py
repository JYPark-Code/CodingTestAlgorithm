n = int(input())
a, b = map(int, input().split())
r = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
result = []


# dfs
def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
