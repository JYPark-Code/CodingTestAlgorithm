def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    div = s // n
    mod = s % n
    # print(mod)
    
    answer = [div] * n
    
    i = 0
    
    while mod > 0:
        answer[i] += 1
        mod -= 1
        i += 1

        if i == len(answer):
            i = 0
            
    answer.sort()
            
    return answer