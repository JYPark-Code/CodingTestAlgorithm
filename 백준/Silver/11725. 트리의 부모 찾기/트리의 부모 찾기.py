import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

parent = [0] * (T+1)
graph = [[] for _ in range(T+1)]
parent[1] = 1

for _ in range(T-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for next_node in graph[node]:
        if parent[next_node] == 0:
            parent[next_node] = node
            dfs(next_node)

dfs(1)
print(*parent[2:], sep="\n")