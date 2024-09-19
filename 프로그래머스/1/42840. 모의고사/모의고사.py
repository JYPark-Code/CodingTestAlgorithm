def solution(answers):
    # 패턴
    a = [1, 2, 3, 4, 5] # 5
    b = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    ac = 0
    bc = 0
    cc = 0
    
    answer = []
    
    for index, num in enumerate(answers):
        if num == a[index % len(a)]:
            ac += 1
            
        if num == b[index % len(b)]:
            bc += 1
            
        if num == c[index % len(c)]:
            cc += 1
        
    # 최대 정답 수 계산
    max_num = max(ac, bc, cc)
    
    # 가장 많이 맞춘 사람의 번호 추가
    if max_num == ac:
        answer.append(1)
        
    if max_num == bc:
        answer.append(2)
        
    if max_num == cc:
        answer.append(3)
        
    return answer
