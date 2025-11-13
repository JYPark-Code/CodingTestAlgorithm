def solution(lines):

    interval = []
    answer = 0

    for line in lines:
        s, e = parse_line(line)
        interval.append((s, e))


    for s, e in interval:

        ws = s
        we = s + 999
        cnt = 0
        for ss, ee in interval:
            if ee > ws and ss <= we:
                cnt += 1
        answer = max(answer, cnt)

        ws = e
        we = e + 999
        cnt = 0
        for ss, ee in interval:
            if ee >= ws and ss <= we:
                cnt += 1
        answer = max(answer, cnt)

    return answer

def time_to_ms(t):
    h, m, s = t.split(":")
    h = int(h)
    m = int(m)
    s = float(s)

    total_seconds = h * 3600 + m * 60 + s
    return total_seconds * 1000

def parse_line(line):
    date, time, process_time = line.split()

    end = time_to_ms(time)

    duration = float(process_time[:-1]) * 1000

    start = end - duration + 1

    return int(start), int(end)
