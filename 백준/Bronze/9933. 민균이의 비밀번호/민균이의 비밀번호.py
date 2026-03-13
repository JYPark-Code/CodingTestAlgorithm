import sys
input = sys.stdin.readline

N = int(input())

mail_content = []
reversed_list = []
for _ in range(N):
    original_text = input().strip()
    mail_content.append(original_text)
    reversed_list.append(original_text[::-1])

for reversed_ in reversed_list:
    if reversed_ in mail_content:
        mid = len(reversed_) // 2
        print(len(reversed_), reversed_[mid])
        break