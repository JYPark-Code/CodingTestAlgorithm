nums = list(map(int, input().split()))

asc = sorted(nums)
des = sorted(nums, reverse=True)

if nums == asc:
    print("ascending")

elif nums == des:
    print("descending")

else:
    print("mixed")