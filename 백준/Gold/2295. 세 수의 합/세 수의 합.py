import sys
import bisect
input = sys.stdin.readline

N = int(input().strip())

arr = []

for _ in range(N):
    arr.append(int(input().strip()))

arr.sort()
two_sums = []

for i in range(N):
    for j in range(i, N):
        two_sums.append(arr[i] + arr[j])

two_sums.sort()
# print(two_sums)

# bisect 사옹하기

for k in range(N-1, -1, -1):
    for j in range(k+1):
        target = arr[k] - arr[j]

        idx = bisect.bisect_left(two_sums, target)

        if idx < len(two_sums) and two_sums[idx] == target:
            print(arr[k])
            exit() # 종료