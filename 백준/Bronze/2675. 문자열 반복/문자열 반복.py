T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    print("".join(ch * R for ch in S))