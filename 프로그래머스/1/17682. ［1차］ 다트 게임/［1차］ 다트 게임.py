import re

def solution(dartResult):
    # S D T = 제곱, * = 2배 (이전과 현재 값), # = 점수 마이너스
    SDT = {"S": 1, "D": 2, "T": 3}
    score_list = []  # 각 점수를 저장할 리스트

    # 1️⃣ **정규식을 활용하여 숫자 + 보너스 + 옵션(선택적) 분리**
    pattern = re.findall(r"(\d+)([SDT])([*#]?)", dartResult)

    for i, (num, bonus, option) in enumerate(pattern):
        num = int(num)  # 문자열 숫자를 정수형으로 변환
        score = num ** SDT[bonus]  # 보너스(S/D/T) 계산

        # 2️⃣ **옵션 처리**
        if option == "*":
            score *= 2
            if i > 0:  # 이전 점수도 2배 처리
                score_list[i - 1] *= 2
        elif option == "#":
            score *= -1  # 점수 마이너스 처리

        score_list.append(score)  # 최종 점수 추가

    return sum(score_list)  # 전체 합 반환
