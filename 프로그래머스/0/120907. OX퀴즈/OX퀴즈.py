def solution(quiz):
    answer = []
    for q in quiz:
        # '='을 기준으로 수식과 결과를 분리합니다.
        expression, expected_result = q.split('=')
        expression = expression.strip()
        expected_result = int(expected_result.strip())

        # 수식을 공백을 기준으로 분리합니다.
        tokens = expression.split()
        
        # 첫 번째 피연산자 설정
        current_value = int(tokens[0])

        # 수식을 왼쪽에서 오른쪽으로 순차적으로 계산합니다.
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            next_number = int(tokens[i + 1])

            if operator == '+':
                current_value += next_number
            elif operator == '-':
                current_value -= next_number

            i += 2  # 다음 연산자를 가리키도록 인덱스 증가

        # 계산 결과와 기대 결과를 비교하여 답안에 추가합니다.
        if current_value == expected_result:
            answer.append('O')
        else:
            answer.append('X')

    return answer
