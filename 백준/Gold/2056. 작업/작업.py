import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

time_list = [0] * (n + 1)

graph = [[] for x in range(n + 1)] # x가 끝났을 때 확인해야 하는 다음 작업들
indegree = [0] * (n + 1)
finish = [0] * (n + 1)

queue = deque()

for i in range(1, n + 1):
    work_table = list(map(int, input().split()))
    time_list[i] = work_table[0]  # 작업 시간
    indegree[i] = work_table[1]  # 기다리는 개수
    required_jobs = work_table[2:]  # 실제 선행 작업 목록


    for pre in required_jobs:
        graph[pre].append(i)

    if indegree[i] == 0:
        queue.append(i)
        finish[i] = time_list[i]

# print(graph)

while queue:
    x = queue.popleft()

    for y in graph[x]:
        if y is None:
            continue
        indegree[y] -= 1
        finish[y] = max(finish[y], finish[x] + time_list[y])

        if indegree[y] == 0:
            queue.append(y)


print(max(finish))