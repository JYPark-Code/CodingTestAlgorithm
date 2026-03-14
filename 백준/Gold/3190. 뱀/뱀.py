from collections import deque
import sys
input = sys.stdin.readline

board_size = int(input())
K = int(input())

apple_coord = set()
for _ in range(K):
    x, y = map(int, input().split())
    apple_coord.add((x, y))

L = int(input())
turn_record = {}
for _ in range(L):
    t, c = input().split()
    turn_record[int(t)] = c

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque([(1, 1)])
snake_set = {(1, 1)}
direction = 0
time = 0

"""
체크리스트
→ 충돌 체크
→ 머리 추가
→ 사과 여부 처리
→ 방향 전환
"""


while True:
    time += 1

    head_x, head_y = snake[-1]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 1) 벽 충돌
    if not (1 <= nx <= board_size and 1 <= ny <= board_size):
        break

    # 2) 몸 충돌
    if (nx, ny) in snake_set:
        break

    # 3) 머리 추가
    snake.append((nx, ny))
    snake_set.add((nx, ny))

    # 4) 사과 여부
    if (nx, ny) in apple_coord:
        apple_coord.remove((nx, ny))
    else:
        tail = snake.popleft()
        snake_set.remove(tail)

    # 5) 방향 전환
    if time in turn_record:
        if turn_record[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)