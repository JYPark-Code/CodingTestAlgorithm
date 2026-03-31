import sys
input = sys.stdin.readline

n, k = map(int, input().split())

sequence = list(map(int, input().split()))
multi_tap = []
answer = 0

# print(sequence)

for idx, plug in enumerate(sequence):
    # 1. 이미 꽂혀 있으면 패스
    if plug in multi_tap:
        continue

    # 2. 빈 자리 있으면 그냥 꽂기
    if len(multi_tap) < n:
        multi_tap.append(plug)
        continue

    # 여기부터 꽂혀있는 거 뽑기
    future = sequence[idx + 1:]

    remove_target = None
    farthest = -1

    for device in multi_tap:
        if device not in future:
            remove_target = device
            break
        else:
            next_pos = future.index(device)
            if next_pos > farthest:
                farthest = next_pos
                remove_target = device

    multi_tap.remove(remove_target)
    multi_tap.append(plug)
    answer += 1

print(answer)