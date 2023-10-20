# DFS, BFS 둘다 사용가능하나, DFS로 처리할 예정
# 책에 아이스크림 얼려먹기에 이동한 좌표 수만 더 세면 됨.
n = int(input())
graph = []
nums = [] # 이동한 좌표만큼 세기

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 넘어갈 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 현재 노드에 방문 하지 않았더라면,
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            nums.append(count)
            result += 1
            count = 0

nums.sort()
print(result)
for i in nums:
    print(i)