def solution(n, m, section):
    count = 0
    current_position = 0

    while current_position < len(section):
        rightmost_covered = section[current_position]
        while current_position < len(section) and section[current_position] <= rightmost_covered + m - 1:
            current_position += 1

        count += 1

    return count
