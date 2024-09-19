def solution(array):
    
    one_string = ''.join(map(str, array))
    # print(one_string)
       
    answer = int(one_string.count('7'))
    return answer