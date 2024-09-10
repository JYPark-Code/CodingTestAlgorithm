def solution(my_string):
    
    num_list = list(map(str, my_string.split()))
    
    # print(num_list)
        
    answer = int(num_list[0])
    
    for i in range(1, len(num_list) - 1):
        if num_list[i] == "+":
            answer += int(num_list[i+1])
        elif num_list[i] == "-":
            answer -= int(num_list[i+1])
    
    return answer