def solution(n, times):
    left, right = 1, max(times) * n
    answer = right  # ✅ 초기값은 가능한 최대값으로 설정

    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)

        if total >= n:  # 가능한 경우
            answer = mid  # ✅ 가능한 값으로 answer 갱신
            right = mid - 1  # 더 작은 시간 찾기
        else:  # 불가능한 경우
            left = mid + 1

    return answer