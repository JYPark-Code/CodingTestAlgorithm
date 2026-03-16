import sys
input = sys.stdin.readline
# a^b % c ?
a, b, c = map(int,(input().split()))

answer = pow(a, b, c)
print(answer) 