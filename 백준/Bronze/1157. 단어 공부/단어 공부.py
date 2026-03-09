from collections import Counter

s = input().upper() # MISSISSIPPI
c = Counter(s)

# 최상위 2개만 뽑아내기 - better
top = c.most_common(2) # [('I', 4), ('S', 4)]

if len(top) > 1 and top[0][1] == top[1][1]:
    print("?")
else:
    print(top[0][0])