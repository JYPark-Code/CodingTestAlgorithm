def solution(array):
    
    max_num = max(array)
    
    for i, num in enumerate(array):
        if num == max_num:
            return [max_num, i]