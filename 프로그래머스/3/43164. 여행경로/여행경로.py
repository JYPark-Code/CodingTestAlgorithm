def solution(tickets):
    
    # 이동 경로는 사전
    flight = dict()

    for ticket in tickets:

        if ticket[0] not in flight:
            flight[ticket[0]] = [ticket[1]]
        else:
            flight[ticket[0]].append(ticket[1])
        
        # 알파벳 순으로 정리
        flight[ticket[0]].sort(reverse=True)
        
    # print(flight)
    
    # 경로 저장 리스트
    answer = []
    
    # DFS 함수 정의
    def dfs(airport):
        # 스택을 이용한 DFS
        while airport in flight and flight[airport]:
            next_airport = flight[airport].pop()  # 도착지를 스택처럼 사용하여 하나씩 pop
            dfs(next_airport)  # 재귀적으로 다음 공항으로 이동
        answer.append(airport)  # 도착지가 없으면 경로에 추가
    
    # 시작점은 "ICN"
    dfs("ICN")
    
    # 경로가 역순으로 쌓였으므로 역순으로 반환
    return answer[::-1]