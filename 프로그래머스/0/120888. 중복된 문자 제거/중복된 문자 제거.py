def solution(my_string):
    
    checklist = []
    answer = ''

    for i in list(my_string):
        if i not in checklist:
            checklist.append(i)
            answer += i
            
    return answer