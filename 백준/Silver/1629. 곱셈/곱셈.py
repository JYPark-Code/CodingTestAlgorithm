import sys
input = sys.stdin.readline
# a^b % c ?
a, b, c = map(int,(input().split()))

# answer = pow(a, b, c)
# print(answer)

if b == 0:
    print(1)
    exit()

answer = 1

while b > 0:

    if b % 2 == 1:
        answer = (answer * a) % c

    a = (a * a) % c

    b //= 2

print(answer)