def solution(ingredient):
    stack = []
    answer = 0
    
    # 리스트의 요소를 하나씩 스택에 추가하면서 패턴이 완성되면 제거
    for i in ingredient:
        stack.append(i)
        
        # 스택의 마지막 4개의 요소가 [1, 2, 3, 1]이면 패턴을 찾은 것
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 마지막 4개 요소 제거
            del stack[-4:]
            answer += 1
    
    return answer
