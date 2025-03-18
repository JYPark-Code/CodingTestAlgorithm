from collections import deque
def solution(board, h, w):
    
    rows = len(board) # x축
    cols = len(board[0]) # y축
    
    visited = [[0] * cols for _ in range(rows) ]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    size = 0
    
    def bfs(x, y):
        
        queue = deque([(x, y)])
        visited[x][y] = 1
        size = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                size += 1
        
        return size
    
    
    size = bfs(h, w)
            
            
    # return size if size > 0 else -1
    return size