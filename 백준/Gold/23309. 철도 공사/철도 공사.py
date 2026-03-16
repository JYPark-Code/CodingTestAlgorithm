import sys
input = sys.stdin.readline

N, M = map(int, input().split())
stations = list(map(int, input().split()))

MAX = 1000001

prev = [0] * MAX
next = [0] * MAX

# 초기 원형 연결
for i in range(N):
    prev[stations[i]] = stations[(i-1) % N]
    next[stations[i]] = stations[(i+1) % N]

answer = []

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "BN":
        i = int(cmd[1])
        j = int(cmd[2])

        nxt = next[i]
        answer.append(str(nxt))

        next[i] = j
        prev[j] = i
        next[j] = nxt
        prev[nxt] = j

    elif cmd[0] == "BP":
        i = int(cmd[1])
        j = int(cmd[2])

        prv = prev[i]
        answer.append(str(prv))

        prev[i] = j
        next[j] = i
        prev[j] = prv
        next[prv] = j

    elif cmd[0] == "CN":
        i = int(cmd[1])

        target = next[i]
        answer.append(str(target))

        nn = next[target]
        next[i] = nn
        prev[nn] = i

    elif cmd[0] == "CP":
        i = int(cmd[1])

        target = prev[i]
        answer.append(str(target))

        pp = prev[target]
        prev[i] = pp
        next[pp] = i

sys.stdout.write("\n".join(answer))