def solution(n, left, right):
    
    # n x n  배열 만들기 -> 메모리 초과 되기 때문에
    # 좌표에 따른 값이 확실하다.
    
    # 좌표 i(row), j(col)를 구하면 값을 바로 구할수 있는게
    # 두 좌표 중에 큰 값 + 1이 해당 좌표의 값이다.
    
    answer = []
    
    for idx in range(left, right + 1):
        i = idx // n # 행 번호
        j = idx % n # 열 번호
        
        answer.append(max(i, j) + 1)
    
    return answer