import sys
input = sys.stdin.readline

N = int(input())
tower_info = list(map(int, input().split()))

t_stack = []
answer = []
answer_idx = -1

for idx, height in enumerate(tower_info):
    answer_idx = idx + 1

    while t_stack and t_stack[-1][1] < height:
        t_stack.pop()

    if not t_stack:
        answer.append(0)

    else:
        answer.append(t_stack[-1][0])

    t_stack.append((answer_idx, height))


print(" ".join(map(str, answer)))