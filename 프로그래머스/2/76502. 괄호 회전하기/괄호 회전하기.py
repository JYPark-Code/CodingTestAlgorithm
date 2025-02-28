def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}  # 괄호 매칭용 딕셔너리
    
    for char in s:
        if char in "({[":
            stack.append(char)  # 여는 괄호는 스택에 push
        elif char in ")}]":
            if not stack or stack[-1] != mapping[char]:  # 짝이 맞지 않으면 False
                return False
            stack.pop()  # 짝이 맞으면 pop
            
    return len(stack) == 0  # 스택이 비어있으면 올바른 괄호 문자열

def solution(s):
    n = len(s)
    count = 0
    
    for i in range(n):  # 문자열을 한 칸씩 회전하면서 검사
        if is_valid(s):
            count += 1
        s = s[1:] + s[0]  # 문자열을 왼쪽으로 한 칸 회전
    
    return count
