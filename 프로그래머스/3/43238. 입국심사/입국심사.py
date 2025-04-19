def solution(n, times):
    
    # n명 대기
    # times = 입국 심사 심사대(index), 심사대 당 걸리는 시간
    
    left = 1
    right = max(times) * n
    
    answer = 0
    
    while left <= right:
        
        mid = (right + left) // 2
        
        total = sum( mid // t for t in times)
        
        if total >= n:
            answer = mid
            right = mid - 1
        
        else:
            left = mid + 1
        
    
    return answer