def solution(rsp):
    winning = {"2":"0", "0":"5", "5":"2"}
    
    answer = ''
    
    for match in rsp:
        answer += winning[match]    
    
    return answer