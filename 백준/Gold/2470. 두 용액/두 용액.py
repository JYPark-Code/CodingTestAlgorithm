import sys
input = sys.stdin.readline

N = int(input())

ph_list = list(map(int, input().split())) # -2 4 -99 -1 98

ph_list.sort()

# print(ph_list) # [-99, -2, -1, 4, 98]
best = float('inf')

ans_left = 0
ans_right = 0

left = 0
right = len(ph_list) - 1

while left < right:
    s = ph_list[left] + ph_list[right]

    if abs(s) < best:
        best = abs(s)
        ans_left = left
        ans_right = right

    if s < 0:
        left += 1
    else:
        right -= 1

print(ph_list[ans_left], ph_list[ans_right])