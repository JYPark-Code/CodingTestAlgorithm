# 크루스칼 쓰고 마지막 날리기

def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n, m : n개의 집 , m개의 연산
n, m = map(int, input().split())

# 부모 노드 초기화
parent = [0] * (n + 1)

# 부모 노드 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    # cost 순으로 정렬
    edges.append((cost, a, b))

# 간선 비용 순으로 정렬
edges.sort()
# 최소 신장트리에서는 마지막이 가장 비용이 큰 간선
last = 0

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우만 집합 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
