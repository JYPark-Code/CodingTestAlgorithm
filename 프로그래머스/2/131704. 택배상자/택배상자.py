from collections import deque

def solution(order):
    queue = deque(range(1, len(order) + 1))  # 1부터 N까지 박스 번호
    sub_rail = []  # 보조 컨베이어 벨트 (스택 역할)
    answer = 0  # 옮긴 박스 수

    for box in order:
        # order[0]가 나올 때까지 queue에서 pop 후 sub_rail에 넣음
        while queue and queue[0] <= box:
            sub_rail.append(queue.popleft())

        # sub_rail의 맨 위 값이 box와 같으면 pop
        if sub_rail and sub_rail[-1] == box:
            sub_rail.pop()
            answer += 1
        else:
            break  # 순서를 맞출 수 없으면 종료

    return answer