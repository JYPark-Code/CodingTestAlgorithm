while True:
    try:
        n = int(input())
    except:
        break

    num = 1  # 1로만 이루어진 수
    count = 1 # 자리수 (10의 제곱수)
    while True:
        if num % n != 0: # n의 배수가 아니라면
            num = num * 10 + 1 # 1로만 이루어진 다음 수
            count += 1 # 자리 수 세기
        else: # n의 배수면
            break  # 종료

    print(count)