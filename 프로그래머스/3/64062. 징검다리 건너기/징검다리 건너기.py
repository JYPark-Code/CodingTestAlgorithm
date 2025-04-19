def solution(stones, k):
    
    def is_possible(mid):
        count = 0  # 연속된 못 밟는 돌의 수

        for stone in stones:
            if stone - mid <= 0:
                count += 1
                if count >= k:
                    return False
            else:
                count = 0  # 끊기면 초기화

        return True
    
    left = 1
    right = max(stones) # 가장 많이 넘어갈 수 있는 건 결국 돌 밟을 수 있는 횟수 Max
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid):  # mid 명이 건널 수 있다면
            answer = mid      # 현재 mid는 가능한 명수 중 하나
            left = mid + 1    # 더 많이 건너볼까?
        else:
            right = mid - 1   # mid는 불가능하므로 줄이자
            
    return answer + 1
        


    