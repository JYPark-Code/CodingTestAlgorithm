def solution(numbers, hand):
    fixed = {"L":[1,4,7,],"R":[3,6,9]}
    
    num_pad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    
    answer = ''
    last_L = '*'
    last_R = '#'
    
    
    for num in numbers:
        if num in fixed["L"]:
            answer += "L"
            last_L = num
            
        elif num in fixed["R"]:
            answer += "R"
            last_R = num
            
        else:
                
            x0, y0 = coordinate(num_pad, num)
            x1, y1 = coordinate(num_pad, last_L)
            x2, y2 = coordinate(num_pad, last_R)

            distance_L = abs(x0 - x1) + abs(y0 - y1)
            distance_R = abs(x0 - x2) + abs(y0 - y2)

            if distance_L == distance_R:
                answer += hand[0].upper()
                
                if hand[0].upper() == "L":
                    last_L = num
                    
                else:
                    last_R = num
                    
            elif distance_L < distance_R:
                answer += "L"
                last_L = num
                
            else:
                answer += "R"  
                last_R = num
                
    return answer

def coordinate(num_pad, input_num):
    for i, row in enumerate(num_pad):
        for j, value in enumerate(row):
            if value == input_num:
                return [i, j]