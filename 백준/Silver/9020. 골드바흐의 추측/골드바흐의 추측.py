import math
import sys
input = sys.stdin.readline

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

T = int(input())

for _ in range(T):
    n = int(input())
    prime_list = []
    for i in range(2, (n // 2) + 1):
        if is_prime(i) and is_prime(n - i):
            prime_list.append([i, n-i])

    if len(prime_list) == 1:
        print(prime_list[0][0], prime_list[0][1])

    else:
        a, b = min(prime_list, key=lambda x: abs(x[0] - x[1]))
        print(a, b)