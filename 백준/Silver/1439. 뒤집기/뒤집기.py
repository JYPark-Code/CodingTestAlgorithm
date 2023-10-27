S = input()

bubble = [S[0]]

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        bubble.append(S[i+1])

zero = bubble.count("0")
one = bubble.count("1")

print(min(zero,one))