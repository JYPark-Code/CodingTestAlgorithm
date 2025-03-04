def solution(citations):
    if not citations:  # 빈 배열이면 0 반환
        return 0
    
    citations.sort(reverse=True)  # 내림차순 정렬
    answer = 0  # 초기값 설정
    
    for idx, c in enumerate(citations):
        if c >= idx + 1:  # 논문 인용 수가 현재 논문의 개수 이상이면 H-Index 후보
            answer = idx + 1
        else:
            break  # 더 이상 증가할 수 없으면 중단
    
    return answer
