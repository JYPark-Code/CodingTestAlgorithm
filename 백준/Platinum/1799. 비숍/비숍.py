import sys
input = sys.stdin.readline

n = int(input())

chessboard = [list(map(int, input().split())) for x in range(n)]
answer = 0
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)
chess_black = []
chess_white = []


# 가능한 후보 만들기
for r in range(n):
    for c in range(n):
        if chessboard[r][c] == 1:
            if (r + c) % 2 == 0:
                chess_black.append((r, c))
            else:
                chess_white.append((r, c))

def dfs(candidate, idx, count):
    global answer
    if idx == len(candidate):
        answer = max(answer, count)
        return

    r, c = candidate[idx]

    d1 = r - c + (n - 1)
    d2 = r + c
    # 1) 놓을 수 있으면 놓기
    if not used_diag1[d1] and not used_diag2[d2]:

        # 체크
        used_diag1[d1] = True
        used_diag2[d2] = True

        dfs(candidate,idx+1, count+1)

        # 체크 해제
        used_diag1[d1] = False
        used_diag2[d2] = False

    # 2) 안 놓기
    dfs(candidate,idx+1, count)

dfs(chess_white,0,0)
white_answer = answer

answer = 0
used_diag1 = [False] * (2*n)
used_diag2 = [False] * (2*n)
dfs(chess_black,0,0)
black_answer = answer

print(white_answer + black_answer)