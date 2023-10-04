def solution(brown, yellow):
    
    # 수식 세워보자.
    # brown = (2 * x) + 2 * (y - 2) = 2 (x * (y - 2))
    # yellow = (x - 2) * (y - 2) 
    
    # 두 수를 더하고 약수를 찾고 위에 수식에 맞는 걸 찾는 방식으로
    
    total = brown + yellow
    
    for b in range(1, total + 1):
        if total % b  == 0:
            a = total // b
            
            if a >= b and 2*a + 2*b - 4 == brown:
                return [a,b]
            