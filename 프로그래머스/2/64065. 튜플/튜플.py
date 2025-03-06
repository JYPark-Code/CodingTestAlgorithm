def solution(s):
    
    answer = []
    
    # print(type(s))
    s_list = convert_string_to_list(s)
    s_list = sorted(s_list, key = lambda x : len(x))
    
    # print(type(s_list))
    
    if len(s_list) == 1:
        return s_list[0]
    
    for num_list in s_list:
         for num in num_list:
                if num not in answer:
                    answer.append(num)

    return answer

def convert_string_to_list(s):
    s = s.strip('{}')  # 바깥쪽 {{}} 제거
    nested_list = [list(map(int, x.split(','))) for x in s.split("},{")]
    
    return nested_list