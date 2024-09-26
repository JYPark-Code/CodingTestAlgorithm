def solution(nums):
    # 최대 선택 가능한 폰켓몬 수
    available = len(nums) // 2
    
    # 고유한 폰켓몬 종류
    set_nums = set(nums)
    
    # 고유한 폰켓몬 종류 수와 선택 가능한 수 중 더 작은 값 반환
    return min(len(set_nums), available)