def solution(number, k):
    stack = []
    for num in number:
        # 현재 숫자가 스택의 top보다 크면 이전 숫자 제거 (가능한 만큼)
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 다 못 뺀 경우 뒤에서 추가로 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
