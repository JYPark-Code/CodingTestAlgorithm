def solution(num, total):
    
    
    # 들어온 숫자가 홀수 일 경우
    if num % 2 == 1:
        mid = total // num # 중앙에 존재할 숫자
        mid_index = num // 2 # 중앙 인덱스
        
        first_num = mid - mid_index
        
        answer = [x for x in range(first_num, first_num + num)]
        return answer
    
    else:
        mid = total // num # 중앙에 존재할 숫자
        mid_index = ( num // 2 ) - 1 # 중앙 인덱스
        
        first_num = mid - mid_index
        
        answer = [x for x in range(first_num, first_num + num)]
        return answer