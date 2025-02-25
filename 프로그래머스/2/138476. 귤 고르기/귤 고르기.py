from collections import Counter

def solution(k, tangerine):
    
    # 1. 귤 크기별 개수 세기
    count = Counter(tangerine)

    # 2. 개수가 많은 순으로 정렬
    sorted_counts = sorted(count.values(), reverse=True)

    # print(sorted_counts)
    
    # 3. k개를 채울 때까지 귤 선택
    total = 0  # 현재 선택한 귤 개수
    kind_count = 0  # 사용한 귤 종류 개수

    for c in sorted_counts:
        total += c
        kind_count += 1
        if total >= k:  # 필요한 개수를 채우면 종료
            return kind_count
