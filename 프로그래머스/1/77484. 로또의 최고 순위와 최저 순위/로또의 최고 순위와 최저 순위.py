def solution(lottos, win_nums):
    
    answer = [0,0]
    
    countZero = lottos.count(0)
    intersected = list(set(lottos).intersection(set(win_nums)))
    matched = len(intersected)
    
    if matched == 0:
        if countZero:
            answer = [1,6]
        else:
            answer = [6,6]
            
    else:   
        answer[0] = 7 - matched
        answer[1] = 7 - (matched + countZero)
        answer.sort()
    return answer