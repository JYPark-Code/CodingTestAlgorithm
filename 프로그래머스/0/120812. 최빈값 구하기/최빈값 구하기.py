def solution(array):
    
    num_dict = dict()
    
    for i in array:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    
    # print(num_dict)
    
    # max(di,key=di.get) # di.get 이용
    
    max_list = [k for k,v in num_dict.items() if max(num_dict.values()) == v] # 리스트 컴프리헨션 이용
    
    print(max_list)
    
    if len(max_list) > 1:
        return -1
    else:
        return max_list[0]