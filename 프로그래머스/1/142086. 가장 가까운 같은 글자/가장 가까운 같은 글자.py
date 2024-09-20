def solution(s):
    answer = []
    save_dict = {}
    
    for i in range(len(s)):
        if s[i] not in save_dict:
            answer.append(-1)
        else:
            answer.append(i - save_dict[s[i]])
        save_dict[s[i]] = i
        
    return answer