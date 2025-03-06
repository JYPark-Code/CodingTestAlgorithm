from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    
    dx = [-1, 1, 0, 0]  # 상하좌우 이동
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, dist = queue.popleft() # 현재 위치
        
        # 도착지에 도착 시 거리 반환
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 맵 범위 안에서 그리고 벽이 아닌 구간에만 이동 숫자
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))
                maps[nx][ny] = 0 # 방문 처리
                
    return -1