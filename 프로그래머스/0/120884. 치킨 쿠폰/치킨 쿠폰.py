def solution(chicken):
    current_coupon = chicken
    answer = 0

    while current_coupon >= 10:
        # 서비스 치킨의 개수를 현재 쿠폰의 수에서 계산
        service_chicken = current_coupon // 10
        # 총 서비스 치킨의 수 추가
        answer += service_chicken
        # 현재 쿠폰의 수를 갱신
        current_coupon = current_coupon - (service_chicken * 10) + service_chicken
    
    return answer
