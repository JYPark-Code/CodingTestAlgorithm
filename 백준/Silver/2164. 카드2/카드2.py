from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

card = [x for x in range(1, N+1)]

card_deque = deque(card)
last = 0

while card_deque:

    if len(card_deque) == 1:
        last = card_deque[0]
        break

    # 첫 장
    card_deque.popleft()
    # 두번째 장
    card_deque.append(card_deque.popleft())

print(last)