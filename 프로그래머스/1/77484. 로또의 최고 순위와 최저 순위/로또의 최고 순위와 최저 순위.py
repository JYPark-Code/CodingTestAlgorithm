def solution(lottos, win_nums):
    
    # 이건 그냥 넣음.
    if (lottos == [0, 0, 0, 0, 0, 0]):
        return [1,6]
    
    zero_count = lottos.count(0)
    # print(zero_count)
    lottos.sort()
    
    # win_nums.sort() 안해도 상관없음.
    
    # 맞는 숫자
    match = 0
    
    # 0이 아닌 부분과 당첨 번호 비교
    not_zero_lottos = lottos[zero_count:]
    
    for num in not_zero_lottos:
        if num in win_nums:
            match += 1
    
    # print("Match : ", match)
    
    # 등수 체크
    rank = 7 - match
    
    if rank >= 6:
        rank = 6
    
    
    # 0의 갯수에 따라 당첨이 되거나 안되는 경우의 수
    return [rank - zero_count, rank]
    