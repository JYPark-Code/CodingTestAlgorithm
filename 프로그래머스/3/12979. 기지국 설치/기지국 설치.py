def solution(n, stations, w):
    answer = 0
    idx = 1  # 아파트 위치 (1부터 시작)
    station_idx = 0  # 현재 기지국 인덱스
    
    while idx <= n:
        # 현재 위치가 기지국 커버 범위 내인지 확인
        if station_idx < len(stations) and idx >= stations[station_idx] - w:
            # 기지국 커버 범위 내이면, 해당 기지국의 커버 끝 부분으로 이동
            idx = stations[station_idx] + w + 1
            station_idx += 1
        else:
            # 커버되지 않은 경우, 새로운 기지국 추가
            answer += 1
            idx += (2 * w + 1)  # 한 번에 커버할 수 있는 최대 거리만큼 이동

    return answer









