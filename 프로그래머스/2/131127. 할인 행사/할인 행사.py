from collections import Counter

def solution(want, number, discount):
    i = 0
    answer = 0
    want_Counter = Counter(dict(zip(want, number)))
    
    # print(want_Counter)
    
    while (i + 10) <= len(discount):
        eval_window = Counter(discount[i:i+10])
        
        if eval_window == want_Counter:
            answer += 1
        
        i += 1
        
    return answer