def solution(elements):
    n = len(elements)
    elements += elements  # 원형 처리를 위해 리스트를 2배로 확장
    unique_sums = set()  # 중복 제거를 위한 set

    for length in range(1, n + 1):  # 부분 수열 길이 (1부터 n까지)
        for start in range(n):  # 시작 인덱스 (0부터 n-1까지)
            unique_sums.add(sum(elements[start:start + length]))  # 슬라이싱 이용
    
    return len(unique_sums)
