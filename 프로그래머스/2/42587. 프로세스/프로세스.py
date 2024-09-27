from collections import deque

def solution(priorities, location):
    # 프로세스 큐: (인덱스, 우선순위)로 구성
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0  # 처리 순서

    while queue:
        # 현재 프로세스를 확인
        cur = queue.popleft()
        
        # 남아 있는 프로세스 중 우선순위가 더 높은 것이 있는지 확인
        if any(cur[1] < q[1] for q in queue):
            # 우선순위가 더 높은 프로세스가 있다면 다시 큐의 끝으로 보냄
            queue.append(cur)
        else:
            # 그렇지 않다면 현재 프로세스를 처리
            answer += 1  # 처리 순서 증가
            # 현재 프로세스가 우리가 찾는 프로세스인 경우
            if cur[0] == location:
                return answer  # 현재 프로세스가 몇 번째로 처리되었는지 반환
