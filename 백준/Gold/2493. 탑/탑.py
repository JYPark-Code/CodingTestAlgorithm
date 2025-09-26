import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []  # (index, height)
answer = []

for i in range(N):
    height = towers[i]

    # 스택에 있는 타워 중, 현재 타워보다 작은 것들은 제거
    while stack and stack[-1][1] < height:
        stack.pop()

    if stack:
        answer.append(stack[-1][0] + 1)  # 1-based index
    else:
        answer.append(0)

    # 현재 타워 push
    stack.append((i, height))

print(*answer)