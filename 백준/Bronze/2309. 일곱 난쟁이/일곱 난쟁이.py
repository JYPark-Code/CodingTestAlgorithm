import itertools

N = 9
dwarfs = []
answer = []

for i in range(N):
    dwarfs.append(int(input()))

nCr = itertools.combinations(dwarfs, 7)
possible_combination = list(nCr)

for j in possible_combination:
    if sum(j) == 100:
        j = sorted(j)
        for dwarf in j:
            print(dwarf)
        break