import math
def solution(n,a,b):
    
    # a, b 가 크기는 모르니 작은 걸 x, 큰걸 y에 적용
    if a > b:
        x = b
        y = a
    else:
        x = a
        y = b
    
    count = 0
    
    # 둘이 붙어있고, y가 짝수번에 나타났을 때
    while True:
        
        count += 1
        
        if y - x == 1 and y % 2 == 0:
            break
        
        x = math.ceil(x/2)
        y = math.ceil(y/2)
        
    return count