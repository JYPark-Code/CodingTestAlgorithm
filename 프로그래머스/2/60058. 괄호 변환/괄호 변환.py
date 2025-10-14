from collections import deque

balanced_parenthesis_string = "()))((()"


def is_correct_parenthesis(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0


def separate_to_u_v(string):  # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:  # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    v = ''.join(list(queue))
    return u, v


def reverse_parenthesis(string):  # 뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def change_to_correct_parenthesis(string):
    if string == '':  # 1번
        return ''
    u, v = separate_to_u_v(string)  # 2번
    if is_correct_parenthesis(u):  # 3번
        return u + change_to_correct_parenthesis(v)
    else:  # 4번
        return '(' + change_to_correct_parenthesis(v) + ')' + reverse_parenthesis(u[1:-1])


def solution(string):
    if is_correct_parenthesis(string):
        return string
    else:
        return change_to_correct_parenthesis(string)
