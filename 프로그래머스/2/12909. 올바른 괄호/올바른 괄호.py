def solution(string):
    answer = True
    stack = []

    for char in string:
        if char == '(':
            stack.append(char)

        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            stack.append(char)

    if stack:
        answer = False

    return answer