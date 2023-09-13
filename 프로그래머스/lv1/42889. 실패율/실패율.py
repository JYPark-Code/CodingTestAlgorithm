def solution(N, stages):
    failure_rates = []

    for stage in range(1, N + 1):
        players_on_stage = stages.count(stage)
        total_players_remaining = len([s for s in stages if s >= stage])

        if total_players_remaining == 0:
            failure_rate = 0
        else:
            failure_rate = players_on_stage / total_players_remaining

        failure_rates.append((stage, failure_rate))

    sorted_failure_rates = sorted(failure_rates, key=lambda x: (-x[1], x[0]))

    result = [stage for stage, _ in sorted_failure_rates]

    return result
