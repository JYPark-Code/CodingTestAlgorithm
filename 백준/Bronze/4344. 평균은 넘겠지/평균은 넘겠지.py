import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    scoreboard = list(map(int, input().split(" ")))
    ppl = scoreboard[0]
    scores = scoreboard[1:]

    # print("사람 수 : ", ppl)
    # print("점수 : ", scores)

    avg = sum(scores) / ppl
    # avg = round((sum(scores) / ppl), 3)

    count = 0
    for score in scores:
        if score > avg:
            count += 1

    answer = count / ppl * 100

    print(f"{answer:.3f}" + "%")