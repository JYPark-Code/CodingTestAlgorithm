import sys
input = sys.stdin.readline

nums_list = list()
for _ in range(9):
    nums_list.append(int(input()))

max_num = max(nums_list)

print(max_num)
print(nums_list.index(max_num) + 1)