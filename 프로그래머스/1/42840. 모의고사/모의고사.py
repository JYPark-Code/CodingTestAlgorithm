def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]  # 각 학생들의 점수를 기록할 리스트

    for idx, ans in enumerate(answers):
        if ans == p1[idx % len(p1)]:
            scores[0] += 1
        if ans == p2[idx % len(p2)]:
            scores[1] += 1
        if ans == p3[idx % len(p3)]:
            scores[2] += 1
        # print(scores)
    max_score = max(scores)  # 가장 높은 점수
    for idx, score in enumerate(scores, 1):
        if score == max_score:
            answer.append(idx)

    return answer