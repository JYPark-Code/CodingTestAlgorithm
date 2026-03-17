import sys
input = sys.stdin.readline

N = int(input())

events = []
stack = []
answer = 1

for _ in range(N):
    x, r = map(int, input().split())
    L = x - r
    R = x + r
    events.append((L, 1, R)) # start
    events.append((R, 0, L)) # end

events.sort(key=lambda x: (x[0], x[1], -x[2]))

# print(events)

# 좌표 시작,종점, 원의 끝점
for pos, type_ , other in events:

    # L, R, last
    if type_ == 1:
        stack.append([pos, other, pos])

    if type_ == 0:
        L, R, last = stack.pop()

        if last == R:
            answer += 2
        else:
            answer += 1

        if stack and stack[-1][2] == L:
            stack[-1][2] = R

print(answer)