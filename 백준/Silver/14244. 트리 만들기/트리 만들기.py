import sys
input = sys.stdin.readline

n, m = map(int, input().split())

"""
Leaf Node를 늘리는 방법을 생각해보자
노드만 늘리기 : 그냥 기존 리프에 붙이면 리프수 변화 X (+1, 0)
내부 노드에 붙이기 : 리프 수 +1 (+1, +1)

전체 답은 n-1개 나오지만 
내부 노드를 k개로 두고
내부 줄기를 만드는데 k-1 (n-m-1) 이 필요.
"""

k = n-m

if k == 1:

    for i in range(1, n):
        print(0, i)

elif k >= 2:

    for i in range(k):
        print(i, i+1)

    leaf = k

    for i in range(k + 1, n):
        print(leaf, i)