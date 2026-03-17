import sys
input = sys.stdin.readline
import heapq

left = [] # Max heap
right = [] # Min heap

N = int(input())

for _ in range(N):

    x = int(input().strip())

    # 길이 기준으로 left에 하나 더
    if len(left) == len(right):
        # left push
        heapq.heappush(left, -x)
    else:
        # right push
        heapq.heappush(right, x)

    # 2. 순서 swap
    if right and -left[0] > right[0]:
        a = -heapq.heappop(left)
        b = heapq.heappop(right)
        heapq.heappush(left, -b)
        heapq.heappush(right, a)


    print(-left[0])