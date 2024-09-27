def solution(s):
    answer = True
    stack = []
    
    for i in s:
        stack.append(i)
        
        if len(stack) >= 2 and stack[-2:] == ['(', ')']:
            del stack[-2:]
    
    if len(stack) > 0:
        return False
    
    return True