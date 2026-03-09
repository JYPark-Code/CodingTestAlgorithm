from collections import Counter

s = input().upper()
c = Counter(s)

max_count = max(c.values())

if list(c.values()).count(max_count) > 1:
    print("?")
else:
    for k, v in c.items():
        if v == max_count:
            print(k)