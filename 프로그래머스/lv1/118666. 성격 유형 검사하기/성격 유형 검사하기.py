def solution(survey, choices):
    # 점수 동일한 경우 사전순으로 빠른 'RCJA'가 기본
    # 1,2,3,4,5,6,7 -> 앞글자 3 - 2 - 1 - 0 - 1 - 2 - 3 뒷글자 포인트로
    # 느낌상 사전이 편해보임.
    
    kakao_mbti = { "R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0 }
    
    for i in range(len(survey)):
        left_ltr = survey[i][0]
        right_ltr = survey[i][1]
        score = choices[i]
        
        if score - 4 > 0:
            kakao_mbti[right_ltr] += (score - 4)
        elif score - 4 < 0:
            kakao_mbti[left_ltr] += abs(score - 4)
    
    # print(kakao_mbti)
            
    answer = ''
    
    if kakao_mbti['R'] >= kakao_mbti['T']:
        answer += "R"
    else:
        answer += "T"
    
    if kakao_mbti['C'] >= kakao_mbti['F']:
        answer += "C"
    else:
        answer += "F"
    
    if kakao_mbti['J'] >= kakao_mbti['M']:
        answer += "J"
    else:
        answer += "M"
    
    if kakao_mbti['A'] >= kakao_mbti['N']:
        answer += "A"
    else:
        answer += "N"
    
    return answer