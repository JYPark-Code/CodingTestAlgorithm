def solution(n, lost, reserve):
    # 중복된 학생 처리
    lost_only = sorted([l for l in lost if l not in reserve])
    reserve_only = sorted([r for r in reserve if r not in lost])

    answer = n - len(lost_only)  # 실제로 체육복이 없는 학생을 제외한 상태에서 시작

    for l in lost_only:
        if l - 1 in reserve_only:
            reserve_only.remove(l - 1)
            answer += 1
        elif l + 1 in reserve_only:
            reserve_only.remove(l + 1)
            answer += 1

    return answer