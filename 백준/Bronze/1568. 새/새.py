N = int(input())
n_num = 1
count = 0

while N > 0:
    if N >= n_num:
        N -= n_num
        n_num += 1
        count += 1
    else:
        n_num = 1

print(count)