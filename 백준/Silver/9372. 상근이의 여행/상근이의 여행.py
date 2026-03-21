import sys
input = sys.stdin.readline

T = int(input()) # 테스트 횟수


for _ in range(T):

    n, m = map(int, input().split())

    for _ in range(m):
        input()
        
    print(n-1)