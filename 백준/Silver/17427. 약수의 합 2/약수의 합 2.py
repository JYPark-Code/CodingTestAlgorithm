n = int(input())

total = 0
for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    total += (n//i)*i

print(total)