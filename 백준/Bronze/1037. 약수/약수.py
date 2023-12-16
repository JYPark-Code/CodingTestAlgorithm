num_count = int(input())
nums = list(map(int, input().split()))

nums.sort()

if num_count == 1:
    print(nums[0] * nums[0])

else:
    print(nums[0] * nums[-1])