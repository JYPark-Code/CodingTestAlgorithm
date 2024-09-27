import copy

def solution(id_list, report, k):
    
    # 동일 리폿 제거
    report = list(set(report))
    # print(report)
                  
    zero = [0 for x in range(len(id_list))]
    
    # 두 리스트로 사전 만들기

    # a = list()
    # b = list()
    # dict_ab = { name: value for name, value in zip(a, b) }
      
    
    report_dict = { name:value for name, value in zip(id_list, zero) }
    answer = copy.deepcopy(report_dict)
    report_name_dict = { }
    
    
    # print(zero)
    
    for r in report:
        user, reported = r.split(' ')
        
        if user not in report_name_dict:
            report_name_dict[user] = [ reported ]
        else:
            report_name_dict[user].append(reported)
        
        if reported in report_dict:
            report_dict[reported] += 1
    
#     print(report_dict)
#     print(report_name_dict)
    
    for key, value in report_name_dict.items():
        
        for reported in value:
            if report_dict[reported] >= k:
                answer[key] += 1
            
        
    # print(answer)
    
    return [x for x in answer.values()]



