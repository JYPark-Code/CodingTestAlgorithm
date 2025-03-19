def solution(m, n, board):
    # 문자열을 리스트로 변환하여 직접 수정 가능하게 변경
    board = [list(row) for row in board]

    while True:
        erase_set = set()  # 지울 블록 집합

        # 1. 2×2 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == '0':  # 빈칸은 제외
                    continue

                # 2×2 블록이 동일한지 확인
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    erase_set |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}

        # 더 이상 지울 블록이 없으면 종료
        if not erase_set:
            break

        # 2. 블록 삭제 (0으로 표시)
        for i, j in erase_set:
            board[i][j] = '0'

        # 3. 중력 적용 (열 별로 블록 내리기)
        for j in range(n):  # 열 별로 탐색
            stack = []
            # 위에서부터 블록을 stack에 쌓음
            for i in range(m):
                if board[i][j] != '0':  # 삭제되지 않은 블록 저장
                    stack.append(board[i][j])

            # 블록을 아래쪽부터 다시 채우기
            for i in range(m - 1, -1, -1):
                board[i][j] = stack.pop() if stack else '0'

    # 4. 삭제된 블록 개수 반환
    return sum(row.count('0') for row in board)
