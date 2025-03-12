def solution(prices):
    stack = []
    answer = [0] * len(prices)  # 정답 배열 미리 생성 (초기값 0)

    for i in range(len(prices)):
        # 가격이 떨어지는 경우, 스택에서 pop하면서 지속 시간 계산
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  # 가격이 유지되지 못한 인덱스 꺼내기
            answer[j] = i - j  # 가격이 유지된 시간 계산
        
        stack.append(i)  # 현재 인덱스 추가
    
    # 스택에 남아 있는 요소들은 끝까지 가격이 유지된 값들
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j  # 끝까지 유지된 경우 처리
    
    return answer
