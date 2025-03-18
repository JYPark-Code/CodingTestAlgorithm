def solution(keymap, targets):
    
    key_dict = {}
    answer = []
    
    for key_seq in keymap:
        for idx , i in enumerate(key_seq):
        
            if i in key_dict:
                if key_dict[i] <= idx + 1:
                    continue
                    
                elif key_dict[i] > idx + 1:
                    key_dict[i] = idx + 1
                    
            elif i not in key_dict:
                key_dict[i] = idx + 1
    
    # print(key_dict)
        
    for target in targets:
        temp = 0
        for i in target:
            
            if i in key_dict:
                temp += key_dict[i]
                
            else:
                temp = -1
                break
        
        answer.append(temp)
                
    return answer