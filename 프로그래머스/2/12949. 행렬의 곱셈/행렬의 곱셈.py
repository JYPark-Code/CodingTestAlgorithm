def solution(arr1, arr2):
    rows_A, cols_A = len(arr1), len(arr1[0])  # arr1의 행과 열 개수
    rows_B, cols_B = len(arr2), len(arr2[0])  # arr2의 행과 열 개수

    # 결과 행렬 초기화 (0으로 채운 2D 리스트)
    result = [[0] * cols_B for _ in range(rows_A)]

    # 행렬 곱셈 수행
    for i in range(rows_A):  # arr1의 행 순회
        for j in range(cols_B):  # arr2의 열 순회
            for k in range(cols_A):  # arr1의 열 = arr2의 행 (공통 차원)
                result[i][j] += arr1[i][k] * arr2[k][j]  # 곱한 값을 더하기

    return result
