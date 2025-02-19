# Greedy + two pointers.
def solution(people, limit):
    
    people.sort()  # 몸무게를 오름차순으로 정렬
    left = 0
    right = len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람도 함께 태움
        right -= 1  # 무거운 사람은 무조건 배에 태우기
        answer += 1  # 배 사용 횟수 증가

    return answer