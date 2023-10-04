def solution(board):
    danger_zone = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    bomb = []
    for row in range(len(board)):
        for col in range(len(board)):
            
            if board[row][col] == 1:
                bomb.append([row, col])
    
    for loc in bomb:
        for zone in danger_zone:
            if 0 <= loc[0] + zone[0] <= len(board) - 1 and 0 <= loc[1] + zone[1] <= len(board) - 1:
                board[loc[0] + zone[0]][loc[1] + zone[1]] = 1
    
    
    
    eval_list = [num for sublist in board for num in sublist ]
    return eval_list.count(0)
    
    
                
        
    
    