def solution(wallpaper):
    # 왼쪽(이쪽도 Max value) 최상단 위 좌표에서 우측(이쪽도 Max value) 최하단 구하면 끝.
    # 대신 Case 3 처럼 한개의 #으로  구성되어있을 경우 처리 다르게 해야함. -> 필요없음
    # 왼쪽 상단은 기존 인덱스대로 처리 우측 하단은 인덱스 [x+1, y+1]로 처리
    # 최상단, 최좌, 최우, 최하단 체크
    
    len_x = len(wallpaper)
    len_y = len(wallpaper[0])
       
    top = 0
    left = len_y - 1
    right = 0
    bottom = 0
    answer = []
    
    # print("left :", left)
    
    for xi, x_string in enumerate(wallpaper):
        # print(xi, x_string)
        # 최적화하기 위해서 '#' 들어갔는지 확인
        if "#" in x_string:
            # 최상단 체크
            if len(answer) == 0:
                answer.append(xi)
                top = xi
                
            # 최하단 체크
            if bottom <= xi:
                bottom = xi + 1
            
            for idx, i in enumerate(x_string):
                if i == "#":
                    if idx <= left:
                        left = idx
                    if idx >= right:
                        right = idx + 1
                    # print(idx, i)
            
    
    # print("top, left, bottom, right", top, left, bottom, right)
    
    # print(answer)
    # print([dx, dy])
    
    
    return [ top, left, bottom, right ]