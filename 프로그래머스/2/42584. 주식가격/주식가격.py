def solution(prices):
    answer = [0] * len(prices)
    stack = []  # (index, price)

    for current_time, current_price in enumerate(prices):
        # 스택에 있는 이전 가격들보다 현재 가격이 낮으면, 떨어진 걸로 간주
        while stack and current_price < prices[stack[-1]]:
            past_time = stack.pop()
            answer[past_time] = current_time - past_time
        stack.append(current_time)

    # 아직 떨어지지 않은 항목들 처리 (끝까지 유지된 가격)
    while stack:
        past_time = stack.pop()
        answer[past_time] = len(prices) - 1 - past_time

    return answer
