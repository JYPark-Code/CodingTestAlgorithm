import heapq

def solution(n, works):
    # n 시간동안 일할 것
    # 피로도는 제곱
    
    if sum(works) <= n:
        return 0
    
    # Max Heap - 힙은 미니 힙이니까, 맥스 힙
    max_heap = [-work for work in works]
    heapq.heapify(max_heap) # O(N)으로 힙 생성
    
    # n 시간 동안 작업량 감소
    for _ in range(n):
        max_val = heapq.heappop(max_heap) # 가장 큰 값 꺼내기 (음수)
        heapq.heappush(max_heap, max_val + 1) # 1 줄인 후 다시 추가
        
    # 남아있는 작업량의 제곱 합 계산
    return sum(x ** 2 for x in max_heap)
    
    
    heapq.heapify(works)
    print(works)
    
    
    answer = 0
    return answer