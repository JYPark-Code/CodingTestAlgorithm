def solution(spell, dic):
    
    set_sorted = list( set(x) for x in dic if len(set(x)) >= len(spell)) # 다 안들어가 있으면 일단 제거
    
    set_spell = set(spell)
    # print(set_spell)
    
    for comparison in set_sorted:
        # print(sorted(set_spell) , sorted(comparison))
        if sorted(set_spell) == sorted(comparison):
            return 1
        
    return 2