from collections import Counter

def solution(N, stages):
    stage_count = Counter(stages)  # 각 스테이지에 머물러 있는 사람 수
    total_players = len(stages)  # 전체 플레이어 수
    
    failure_rates = []  # (실패율, 스테이지) 리스트

    for stage in range(1, N + 1):  # 1 ~ N 스테이지 순회
        if total_players == 0:  # 모든 플레이어가 클리어한 경우
            failure_rates.append((0, stage))
        else:
            fail_rate = stage_count[stage] / total_players  # 실패율 계산
            failure_rates.append((fail_rate, stage))
            total_players -= stage_count[stage]  # 남은 유저 업데이트

    # 실패율을 기준으로 내림차순 정렬, 실패율이 같다면 스테이지 번호 오름차순
    failure_rates.sort(key=lambda x: (-x[0], x[1]))

    # 스테이지 번호만 반환
    return [stage for _, stage in failure_rates]
