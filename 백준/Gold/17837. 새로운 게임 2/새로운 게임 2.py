# 첫 줄 입력
n, k = map(int, input().split())

# 체스판 정보 입력
chess_map = [list(map(int, input().split())) for _ in range(n)]

# 말의 위치 및 방향 정보 입력 (★ 1-based -> 0-based로 변환)
horses = []
for _ in range(k):
    r, c, d = map(int, input().split())
    horses.append([r-1, c-1, d-1])  # ★ 포인트

dr = [0, 0, -1, 1]  # 0:→, 1:←, 2:↑, 3:↓
dc = [1, -1, 0, 0]

MAX = 1000

def reverse_direction(d):
    if d == 0: return 1
    if d == 1: return 0
    if d == 2: return 3
    if d == 3: return 2
    return d

def get_game_over_turn_count(horse_count, game_map, horses):
    N = len(game_map)

    # 각 칸의 스택: 말 index(0-based) 리스트
    stacks = [[[] for _ in range(N)] for _ in range(N)]
    for idx, (r, c, _) in enumerate(horses):
        stacks[r][c].append(idx)

    def out(r, c):
        return r < 0 or r >= N or c < 0 or c >= N

    for turn in range(1, MAX + 1):
        for i in range(horse_count):
            r, c, d = horses[i]

            nr, nc = r + dr[d], c + dc[d]

            # 파랑/벽: 방향 반전 후 한 번 더 시도
            if out(nr, nc) or game_map[nr][nc] == 2:
                d = reverse_direction(d)
                horses[i][2] = d  # 방향만 갱신
                nr, nc = r + dr[d], c + dc[d]
                # 여전히 파랑/벽이면 이동하지 않음
                if out(nr, nc) or game_map[nr][nc] == 2:
                    continue

            # 현재 칸에서 i와 그 위의 말들을 떼기
            cur = stacks[r][c]
            pos = cur.index(i)
            moving = cur[pos:]  # i 포함 위의 덩어리
            stacks[r][c] = cur[:pos]  # 아래 남은 스택

            # 목적지 색 처리
            color = game_map[nr][nc]
            if color == 1:  # 빨강: 덩어리만 역순
                moving.reverse()
            # 흰(0)은 그대로, 파랑(2)은 위에서 걸러짐

            # 이동 반영 (좌표 갱신)
            for m in moving:
                horses[m][0], horses[m][1] = nr, nc
            stacks[nr][nc].extend(moving)

            # 종료 조건: 어느 칸이든 4개 이상
            if len(stacks[nr][nc]) >= 4:
                return turn

    return -1

print(get_game_over_turn_count(k, chess_map, horses))
