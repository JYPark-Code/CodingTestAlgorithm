def solution(n):
    # 인터넷 찾아보니 재귀를 쓰라고 함.
    answer = []
    
    def hanoi(start, target, middle, n):
        # 한 개일 경우 공식 쓸 필요 없이 바로 이동
        if n == 1:
            answer.append([start, target])
        else:
            hanoi(start,middle,target,n-1) # 1번에서 2번까지 n-1개의 원판을 이동 (재귀로 이동)
            hanoi(start,target,middle,1) # 1번에서 가장 큰 원판 3번으로 이동
            hanoi(middle,target,start,n-1) # 2번에서 마지막 파트로 원판 이동 (재귀로 이동)
            
    hanoi(1,3,2,n)
            
    return answer