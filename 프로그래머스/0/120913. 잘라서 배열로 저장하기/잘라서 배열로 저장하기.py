def solution(my_str, n):
    
    answer = []
    total_length = len(my_str)
    quotient = total_length // n
    last_index = quotient * n
    
    
    for i in range(quotient):
        answer.append("".join(my_str[ i * n : ((i + 1) * n)]))
    
    # 깔끔하게 나누어졌을 때
    if total_length % n == 0:
        return answer
    
    # 나머지 있을 때
    # print(last_index)
    answer.append("".join(my_str[last_index:]))
    return answer