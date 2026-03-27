import sys
input = sys.stdin.readline

string_input = input().strip()
part = string_input.split("-")
# print(part)
groups = [[] for _ in part]

for idx, p in enumerate (part):
    nums = p.split("+")
    for num in nums:
        if num.isnumeric():
            groups[idx].append(int(num))

# print(groups)

answer = sum(groups[0])

for i in range(1, len(groups)):
    answer -= sum(groups[i])

print(answer)