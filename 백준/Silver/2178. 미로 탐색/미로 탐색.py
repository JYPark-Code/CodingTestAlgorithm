from collections import deque

# n, m 입력받기
n, m = map(int, input().split())
# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1 ,0, 0]
dy = [0, 0 ,-1, 1]


# BFS
def bfs(x, y):
    # Queue
    queue = deque()
    queue.append((x, y))
    # 큐 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
