import sys
input = sys.stdin.readline

computers = int(input())
links = int(input())
graph = [[] for _ in range(computers+1)]

visited = set()

for _ in range(links):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for next_node in graph[node]:
        if next_node not in visited:
            visited.add(next_node)
            dfs(next_node)

visited.add(1)
dfs(1)
# print(graph)
# print(visited)
print(len(visited) - 1)