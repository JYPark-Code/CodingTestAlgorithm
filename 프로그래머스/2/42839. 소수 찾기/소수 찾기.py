from itertools import permutations # 순열
import math

def solution(numbers):
    
    num_list = list(x for x in numbers)
    eval_num_list = list() # 겹치는 숫자 방지
    count = 0
    
    for i in range(1, len(num_list) + 1):
        for j in permutations(num_list, i):
            # print(list(j))
            
            eval_num = int(''.join(list(j)))
            # print(eval_num)
            
            if eval_num not in eval_num_list:
                if is_prime_number(eval_num):
                    eval_num_list.append(eval_num)
                    count += 1
            
            
    
    
    # print(num_list)
    
    # answer = 0
    return count



# 소수 판별 함수
def is_prime_number(x):
    
    if x <= 1:
        return False # 소수가 아님
    
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임