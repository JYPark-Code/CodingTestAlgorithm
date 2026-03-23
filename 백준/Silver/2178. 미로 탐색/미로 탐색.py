import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

# print(maze)

# 방향 : 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있을 때만 계산
        if 0 <= nx < n and 0 <= ny < m:

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

print(maze[n-1][m-1])