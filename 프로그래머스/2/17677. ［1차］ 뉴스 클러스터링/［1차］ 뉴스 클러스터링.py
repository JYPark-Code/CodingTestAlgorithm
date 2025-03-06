from collections import Counter

def solution(str1, str2):
    
    # 대소문자 무시, 특수문자, 공백 시, 쌍으로 날린다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2:
        return 65536
    
    double_list1 = making_double_list(str1)
    double_list2 = making_double_list(str2)
    
    counter1 = Counter(double_list1)
    counter2 = Counter(double_list2)
    
    # print(counter1)
    # print(counter2)
    
    inter_set = sum((counter1 & counter2).values())  # 교집합 크기
    union_set = sum((counter1 | counter2).values())  # 합집합 크기

    return int((inter_set / union_set) * 65536) if union_set > 0 else 65536


def making_double_list(s):
    double_list = list()
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            double_list.append(s[i:i+2])
        
    return double_list
    