def solution(nums):
    
    total = len(nums)
    
    max_choice = total // 2
    
    sorted_nums = set(nums)
    
    # print(sorted_nums)
    
    if len(sorted_nums) > max_choice:    
        return max_choice
    
    else:
        return len(sorted_nums)
        
    
    # answer = 0
    # return answer