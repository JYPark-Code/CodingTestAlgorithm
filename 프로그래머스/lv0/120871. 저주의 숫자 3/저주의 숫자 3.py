def solution(n):
    
    threeX = list()
    i = 1
    
    while len(threeX) != n:
        if i % 3 == 0 or '3' in str(i):
            i += 1
            continue
        threeX.append(i)
        i += 1
    
    # print(threeX)
    
    return threeX[n-1]