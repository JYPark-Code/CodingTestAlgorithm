import sys
input = sys.stdin.readline

# 게임 구역
N = int(input().strip())

jelly_map = [list(map(int, input().split())) for _ in range(N)]

# 가능한 이동 경로 오른쪽, 아래
dx = [1, 0]
dy = [0, 1]

def dfs(x,y):
    if x >= N or y >= N:
        return False

    if jelly_map[x][y] == -1:
        return True
    
    k = jelly_map[x][y]

    if k == 0:
        return False
    
    for i in range(2):
        nx = x + dx[i] * k
        ny = y + dy[i] * k

        if dfs(nx, ny):
            return True

    return False

if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")