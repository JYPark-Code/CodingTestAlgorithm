def solution(numbers, target):
    leaves = [0]               
    count = 0 

    for num in numbers : 
        temp = []
	
        # 자손 노드 
        for leaf in leaves : 
            temp.append(leaf + num)    # 더하는 경우 
            temp.append(leaf - num)    # 빼는 경우 

        leaves = temp
    
    # print(leaves)
    
    return leaves.count(target)