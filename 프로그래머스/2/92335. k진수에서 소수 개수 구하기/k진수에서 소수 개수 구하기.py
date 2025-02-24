import math

def solution(n, k):
    answer = 0
    number = number_convert(n, k)
    # print(type(number))
    number_list = [x for x in number.split('0') if x != '1' and x != '']
    
    # print(number_list)
    
    for num in number_list:
        num = int(num)
        if is_primenum(num):
            answer += 1
    
    return answer


#x가 소수인지 확인하는 알고리즘
def is_primenum(x): 
    for i in range (2, int(math.sqrt(x)) + 1):
    	if x % i == 0:
        	return False
    return True


# 진수 변환 -> str로 리턴
def number_convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]