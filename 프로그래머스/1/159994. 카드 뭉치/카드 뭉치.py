def solution(cards1, cards2, goal):
    c1 = 0  # cards1의 인덱스
    c2 = 0  # cards2의 인덱스
    
    for word in goal:
        # cards1에서 현재 단어를 찾는 경우
        if c1 < len(cards1) and word == cards1[c1]:
            c1 += 1
        # cards2에서 현재 단어를 찾는 경우
        elif c2 < len(cards2) and word == cards2[c2]:
            c2 += 1
        # 둘 다 아닐 경우 순서가 맞지 않음
        else:
            return "No"
    
    # 모든 단어가 순서에 맞게 처리된 경우
    return "Yes"
