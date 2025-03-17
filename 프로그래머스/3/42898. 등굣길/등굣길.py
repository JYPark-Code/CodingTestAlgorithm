def solution(m, n, puddles):
    MOD = 1000000007  # 나머지 연산을 위한 값

    # DP 테이블 초기화 (0으로 채우기)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 웅덩이 위치 설정 (0과 구별하기 위해 -1)
    for x, y in puddles:
        dp[y][x] = -1  

    # 시작 위치 (1,1) 초기화
    dp[1][1] = 1  

    # DP 테이블 채우기
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if dp[y][x] == -1:  # 웅덩이인 경우, 경로를 0으로 설정
                dp[y][x] = 0
                continue

            # 첫 번째 행과 첫 번째 열 처리 (웅덩이 고려)
            if x > 1:
                dp[y][x] += dp[y][x - 1]
            if y > 1:
                dp[y][x] += dp[y - 1][x]
                
            # 큰 숫자 방지
            dp[y][x] %= MOD

    return dp[n][m]
