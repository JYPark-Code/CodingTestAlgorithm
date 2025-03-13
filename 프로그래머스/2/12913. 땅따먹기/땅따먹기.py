def solution(land):
    for i in range(1, len(land)):  # 두 번째 행부터 시작
        max1, max2 = 0, 0
        max1_index = -1

        # 이전 행에서 최댓값(max1)과 두 번째 최댓값(max2)을 찾음
        for j in range(4):
            if land[i - 1][j] > max1:
                max2 = max1  # 기존 max1을 max2로 이동
                max1 = land[i - 1][j]
                max1_index = j
            elif land[i - 1][j] > max2:
                max2 = land[i - 1][j]

        # 현재 행을 업데이트
        for j in range(4):
            # 현재 선택한 열이 이전 행에서 최댓값을 가졌다면 max2 사용, 아니면 max1 사용
            land[i][j] += max2 if j == max1_index else max1

    return max(land[-1])  # 마지막 행에서 최대값 선택
