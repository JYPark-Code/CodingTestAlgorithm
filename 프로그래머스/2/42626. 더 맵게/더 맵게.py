import heapq

def solution(scoville, K):
    
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    count = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) 
        heapq.heappush(scoville, a + (b*2))
        count += 1
        
    return count if scoville[0] >= K else -1