def solution(answers):
    
    pattern = {
        1:[1, 2, 3, 4, 5],
        2:[2, 1, 2, 3, 2, 4, 2, 5],
        3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    
    matched = [0] * 4
    
    for guy in pattern :
        for idx, ans in enumerate(answers):
            if pattern[guy][idx % (len(pattern[guy]))] == ans:
                matched[guy] += 1
    
    answer = []
    
    for idx, i in enumerate(matched): 
        if i == max(matched):
            answer.append(idx)
    
    return answer