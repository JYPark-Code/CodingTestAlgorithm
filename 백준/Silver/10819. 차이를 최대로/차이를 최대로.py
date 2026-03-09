import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

max_value = 0

for p in permutations(arr):
    total = 0

    for i in range(N-1):
        total += abs(p[i] - p[i+1])

    max_value = max(max_value, total)

print(max_value)