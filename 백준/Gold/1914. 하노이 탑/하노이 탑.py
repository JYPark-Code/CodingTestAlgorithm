import sys
input = sys.stdin.readline

n = int(input())
count = 2 ** n - 1

def move(no, x, y):
    global count

    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(x, y)

    if no > 1:
        move(no - 1, 6 - x - y, y)


print(count)
if n <= 20:
    move(n,1, 3)