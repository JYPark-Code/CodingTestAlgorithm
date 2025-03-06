from itertools import permutations

def solution(k, dungeons):
        
    possible_sequence = list(permutations(dungeons, len(dungeons)))
    
    answer = -1
    
    for d_list in possible_sequence:
        copied_k = k
        count = 0
        
        for d in d_list:
            
            if d[0] <= copied_k:
                copied_k -= d[1]
                count += 1
                
                if count == len(dungeons):
                    return count
                     
            if answer < count:
                answer = count
    
    
    return answer