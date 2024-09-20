def solution(s):
    
    num_list = 	['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']    
    temp = ""
    result = ""
    
    for i in range(len(s)):
        c = s[i]
        
        if(c.isnumeric()):
            result += c
        
        else:
            temp += c
            if temp in num_list:
                result += str(num_list.index(temp))
                temp = ""
                
    return int(result)        
