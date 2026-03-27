import sys
input = sys.stdin.readline

N = int(input().strip())

meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))
    
meetings.sort(key= lambda x: (x[1], x[0]))
selected = [meetings[0]]
last_end = meetings[0][1]

for meeting in meetings[1:]:
    start, end = meeting
    if start >= last_end:
        selected.append(meeting)
        last_end = end

print(len(selected))