import sys
input = sys.stdin.readline

# BFS 아님 정사각형 길이가 정해져 있음
## 연속으로 / 4 하면 나오는 정사각형 크기 정해짐

N = int(input().strip())

# 2차 배열 넣기
square_info = [list(map(int, input().split())) for x in range(N)]

# print(square_info)
white_list = 0
blue_list = 0

# 시작 좌표, 그리고 정사각형의 길이
def solve(x, y, size):
    global white_list,blue_list
    first = square_info[x][y]

    for i in range(x, x + size):
        for j in range(y, y+ size):
            if square_info[i][j] != first:
                # 4등분 재귀
                half = size // 2
                solve(x, y, half)
                solve(x, y + half, half)
                solve(x + half, y, half)
                solve(x + half, y + half, half)
                return

    if first == 0:
        white_list += 1
    else:
        blue_list += 1

solve(0, 0, N)
print(white_list)
print(blue_list)