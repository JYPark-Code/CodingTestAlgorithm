def solution(n, t, m, p):
    # 진법, 미리 구할 숫자 갯수(result의 length), 참가 인원, 튜브 순서
    
    wanted_number = ""
    num = 0
    answer = ''
    
    while len(wanted_number) < (m * t):
        wanted_number += convert(num, n)
        num += 1
    
    for i in range(p-1, m * t, m):
        answer += wanted_number[i]

    return answer

def convert(num, base):
    digits = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
        
    return result if result else "0" # num이 0일 땐 0