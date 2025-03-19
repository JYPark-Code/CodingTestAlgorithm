from collections import Counter

def solution(X, Y):
    cx = Counter(X)
    cy = Counter(Y)
    common = cx & cy
    
    answer = []
    
    if not common:
        return "-1"
    
    #  .elements() 사용하여 개수만큼 숫자 확장 후, 정렬
    result = ''.join(sorted(common.elements(), reverse=True))
    
    if len(result) > 1 and result[0] == '0':
        return '0'

    return result