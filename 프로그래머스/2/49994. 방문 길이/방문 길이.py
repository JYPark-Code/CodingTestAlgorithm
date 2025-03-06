def solution(dirs):
    
    move = ["U", "D", "R", "L"]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 , 0]
    
    visited_paths = set()
    
    answer = 0
    prev = (0, 0) # 시작점
    
    for dir in dirs:
        
        i = move.index(dir)
        
        if -5 <= prev[0] + dx[i] <= 5 and -5 <= prev[1] + dy[i] <= 5:
            next = (prev[0] + dx[i], prev[1] + dy[i])
            
            if (prev, (prev[0] + dx[i], prev[1] + dy[i])) not in visited_paths and ((prev[0] + dx[i], prev[1] + dy[i]), prev) not in visited_paths:
                # (이전 위치 → 현재 위치)와 (현재 위치 → 이전 위치) 모두 저장
                visited_paths.add((prev, next))
                visited_paths.add((next, prev))

                # 카운트 증가
                answer += 1

            # print("전: ", prev, "후: ", next)
            # print(answer)

        # 이전 좌표를 갱신
        prev = next
        
    
    return answer