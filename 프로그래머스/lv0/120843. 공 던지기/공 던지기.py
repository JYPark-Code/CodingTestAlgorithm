def solution(numbers, k):
    
    # 0 + 2 * (k-1)

    return numbers[(2*(k-1)) % len(numbers)]