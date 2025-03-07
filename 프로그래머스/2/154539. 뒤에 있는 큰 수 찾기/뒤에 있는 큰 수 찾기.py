def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)  # 기본값 -1로 초기화

    for i in range(len(numbers) - 1, -1, -1):  # 뒤에서부터 탐색
        while stack and stack[-1] <= numbers[i]:  # 현재 값보다 작은 값은 pop
            stack.pop()
        
        if stack:  # 스택이 비어있지 않다면, 다음 큰 수 존재
            answer[i] = stack[-1]
        
        stack.append(numbers[i])  # 현재 값을 스택에 추가

    return answer
