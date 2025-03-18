def solution(A, B):
    
    answer = 0
    A.sort()
    B.sort()
    
    i, j = 0, 0  # 투 포인터 사용
    while i < len(A) and j < len(B):
        if B[j] > A[i]:  # A를 이길 수 있는 경우
            answer += 1
            i += 1  # A의 다음 경기로 이동
        j += 1  # B의 다음 선수를 선택

    return answer