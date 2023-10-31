def solution(s):
    answer = len(s)
    # 1개부터 압축 단위 늘리기
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        # 단위(step) 크기 만큼 증가 시키고 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축(count) 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면 or 압축을 못하는 경우
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 상태 다시 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev

        # 제일 짧은게 정답
        answer = min(answer, len(compressed))
    return answer