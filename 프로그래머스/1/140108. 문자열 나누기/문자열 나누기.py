def solution(s):
    # 초기 변수 설정
    x = s[0]
    x_count = 1
    others = 0
    answer = 0
    
    for i in range(1, len(s)):
        if x != s[i]:
            others += 1
        else:
            x_count += 1
        
        # x와 다른 문자의 개수가 같을 때
        if x_count == others:
            answer += 1
            x_count = 0
            others = 0
            # 새로운 그룹의 첫 번째 문자 설정
            if i < len(s) - 1:
                x = s[i + 1]
    
    # 마지막 그룹이 남아 있을 때 처리
    if x_count != 0 or others != 0:
        answer += 1
    
    return answer
