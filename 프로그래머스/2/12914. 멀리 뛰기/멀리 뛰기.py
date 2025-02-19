def solution(n):
    '''
    그냥 피보나치 수열 문제였다.
    조합으로 풀면 더 복잡해진다.
    '''
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, (a + b) % 1234567
    return a