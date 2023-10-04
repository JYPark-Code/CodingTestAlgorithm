# stack 이용하면 쉽게 푼다. 라고 찾음.

def solution(s):
    # copied_s = s
    eval_list = list()
    
    for i in s:
        
        if len(eval_list) == 0:
            eval_list.append(i)
        
        elif eval_list[-1] == i:
            eval_list.pop()
        
        else:
            eval_list.append(i)
        
    if len(eval_list) == 0:
        return 1
    
    return 0
    