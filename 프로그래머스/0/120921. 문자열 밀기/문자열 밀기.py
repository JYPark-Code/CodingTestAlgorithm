def solution(A, B):
    
    if A == B:
        return 0
    
    return (B * 2).find(A)