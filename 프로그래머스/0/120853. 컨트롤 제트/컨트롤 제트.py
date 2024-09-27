def solution(s):
    num = list(s.split(' '))
    eval_list = list()
    
    for i in num:
        
        if i == 'Z':
            eval_list.pop()
        
        else:
            eval_list.append(int(i))
            
    # print(eval_list)
    
    # answer = 0
    if len(eval_list) == 0:
        return 0
    
    return sum(eval_list)