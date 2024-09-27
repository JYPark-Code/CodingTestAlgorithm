import math

def solution(progresses, speeds):
    answer = []
    
    # 각 기능이 완료되는 데 걸리는 시간을 계산
    takes = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 첫 번째 기능의 완료 시간을 기준으로 배포 시점을 판단
    first = takes[0]
    count = 0
    
    for t in takes:
        if t <= first:
            count += 1  # 배포 가능한 기능 수 증가
        else:
            answer.append(count)  # 배포 가능한 기능들을 한꺼번에 배포
            count = 1  # 새로운 배포 그룹 시작
            first = t  # 새로운 배포 기준 시간 업데이트
    
    answer.append(count)  # 마지막 배포 그룹 추가
    
    return answer
