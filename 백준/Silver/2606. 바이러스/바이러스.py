# 1번 컴퓨터 감염, DFS 문제로 판단

comp = int(input())
node = int(input())

graph = [[] for _ in range(comp + 1)]

for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# 노드 방문 여부
visited = [False] * (comp + 1)


# 연결된 노드 다 방문 하기
def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(1)
# print(visited)
print(sum(visited) - 1)