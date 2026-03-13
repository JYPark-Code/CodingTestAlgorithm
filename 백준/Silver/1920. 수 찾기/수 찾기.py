import sys
input = sys.stdin.readline

N = int(input().strip())
A_list = sorted(map(int, input().split()))

M = int(input().strip())
B_list = list(map(int, input().split()))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1

        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return 0

for b in B_list:
    print(binary_search(A_list, b))