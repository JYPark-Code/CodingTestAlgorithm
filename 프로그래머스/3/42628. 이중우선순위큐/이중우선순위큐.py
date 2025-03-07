import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}  # 유효한 값만 저장 (동기화용)

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == 'I':  # 값 삽입
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            entry_finder[value] = entry_finder.get(value, 0) + 1  # 값 개수 카운트

        elif command == 'D' and entry_finder:  # 값 삭제 (힙이 비어있지 않을 경우만)
            if value == 1:  # 최댓값 삭제
                while max_heap and entry_finder.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)  # 무효값 정리
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] -= 1

            elif value == -1:  # 최솟값 삭제
                while min_heap and entry_finder.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)  # 무효값 정리
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] -= 1

    # 마지막 정리: 실제로 유효한 값만 남기기
    while min_heap and entry_finder.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_finder.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    return [0, 0] if not min_heap else [-max_heap[0], min_heap[0]]
