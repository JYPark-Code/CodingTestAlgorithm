def solution(numbers):
    # 숫자를 문자열로 바꾸고
    numbers = list(map(str, numbers))
    
    # 문자열끼리 x+y, y+x를 비교해서 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)

    # '0'으로만 이루어졌다면 '0' 리턴
    return '0' if numbers[0] == '0' else ''.join(numbers)