def solution(i, j, k):
    answer = 0
    
    for x in range(i, j + 1):
        answer += list(map(int, str(x))).count(k)
        # print(x, answer)
        
    return answer