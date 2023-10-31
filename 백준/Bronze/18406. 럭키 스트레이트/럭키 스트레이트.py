num = [int(x) for x in input()]

length = len(num)

if sum(num[: length // 2]) == sum(num[length // 2:]):
    print("LUCKY")
else:
    print("READY")