def solution(skill, skill_trees):
    # skill -> 선행순서, skill_trees 사용자들이 시도하려는 스킬트리
    
    
    answer = 0
    
    for tree in skill_trees:
        
        sequence = 0
        is_valid = True
        
        for s in tree:
            if s in skill:
                
                if skill.index(s) == sequence:
                    sequence += 1
                
                else:
                    is_valid = False
                    break
                    
        if is_valid:
            answer += 1
                            
    return answer