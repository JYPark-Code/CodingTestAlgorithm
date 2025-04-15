from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (0은 빈칸)
    truck_weights = deque(truck_weights) # 남은 대기 트럭
    time = 0
    bridge_weight = 0  # 현재 다리 위 총 무게

    while bridge:
        time += 1
        # 1초 지나면 앞에서 트럭이 하나 나감
        out = bridge.popleft()
        bridge_weight -= out

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)  # 못 올라오면 0 추가
    return time
