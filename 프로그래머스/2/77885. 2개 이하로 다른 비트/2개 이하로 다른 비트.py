def solution(numbers):
    
    answer = []
    
    for num in numbers:
        # 짝수일땐 그냥 +1
        if num % 2 == 0:
            answer.append(num + 1)
            
        else:
            # 1. num의 0이 아닌 비트 위치를 찾기 위해
            # 2. num ^ (num + 1)은 바뀐 비트 위치를 알려줌
            # 3. 그 위치를 오른쪽으로 2만큼 나누면 바뀐 비트의 개수를 줄임
            bit = (num ^ (num + 1)) >> 2
            answer.append(num + 1 + bit)
    
    return answer