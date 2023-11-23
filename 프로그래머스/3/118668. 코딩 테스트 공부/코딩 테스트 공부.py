import heapq


def solution(alp, cop, problems):
    pq = []

    max_alp = 0
    max_cop = 0
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    visited = [[False] * (max_cop + 1) for _ in range(max_alp + 1)]

    alp = min(max_alp, alp)
    cop = min(max_cop, cop)

    new_problems = problems[:]
    new_problems.insert(0, [0, 0, 1, 0, 1])
    new_problems.insert(0, [0, 0, 0, 1, 1])

    heapq.heappush(pq, (0, alp, cop))
    while pq:
        cur_time, cur_alp, cur_cop = heapq.heappop(pq)
        if visited[cur_alp][cur_cop]:
            continue
        visited[cur_alp][cur_cop] = True

        # base case
        if max_alp <= cur_alp and max_cop <= cur_cop:
            return cur_time

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in new_problems:
            if cur_alp >= alp_req and cur_cop >= cop_req:
                heapq.heappush(
                    pq,
                    (
                        cur_time + cost,
                        min(max_alp, cur_alp + alp_rwd),  # max_alp 범위를 넘어서지 않게 제한
                        min(max_cop, cur_cop + cop_rwd),  # max_cop 범위를 넘어서지 않게 제한
                    ),
                )

    return 0