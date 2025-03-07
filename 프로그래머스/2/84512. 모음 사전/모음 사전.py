def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    weight = [781, 156, 31, 6, 1]  # 자리별 가중치

    answer = 0
    for i in range(len(word)):
        answer += alpha.index(word[i]) * weight[i] + 1  # 해당 자리의 가중치 적용 + 1

    return answer