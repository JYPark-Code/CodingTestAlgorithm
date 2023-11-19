n = input()
m = input()

count = 0
search = 0

while search < len(n):
    if n[search:(search + len(m))] == m and search + len(m) <= len(n):
        count += 1
        search += len(m)

    elif n[search:(search + len(m))] != m and search + len(m) <= len(n):
        search += 1

    elif search + len(m) > len(n):
        break

print(count)