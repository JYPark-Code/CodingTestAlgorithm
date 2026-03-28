import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

i = len(A)
j = len(B)

L = [[0] * (j+1) for _ in range(i+1)]

if i == 0 or j == 0:
    print(0)
    exit()

for x in range(1, i+1):
    for y in range(1, j+1):
        if A[x-1] == B[y-1]:
            L[x][y] = L[x-1][y-1] + 1
        else:
            L[x][y] = max(L[x-1][y], L[x][y-1])

print(L[i][j])