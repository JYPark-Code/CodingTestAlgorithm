from collections import Counter

def solution(topping):
    
    answer = 0
    
    right_count = Counter(topping)
    left_count = Counter()
    
    right_unique = len(right_count)
    left_unique = 0
    
    for t in topping:
        
        left_count[t] += 1
        if left_count[t] == 1:
            left_unique += 1
        
        right_count[t] -= 1
        if right_count[t] == 0:
            right_unique -= 1
            
        if left_unique == right_unique:
            answer += 1
            
    return answer