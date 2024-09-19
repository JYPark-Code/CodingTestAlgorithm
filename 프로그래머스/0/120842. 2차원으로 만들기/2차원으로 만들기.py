def solution(num_list, n):
    answer = []
    total_length = len(num_list)
    repeat = total_length // n
    
    for i in range(repeat):
        answer.append(num_list[(i*n):(i*n)+n])
        
    return answer