def solution(msg):
    words = {chr(i + 65): i + 1 for i in range(26)}  # 초기 사전 (A~Z)
    next_index = 27  # 다음 등록될 인덱스 번호
    answer = []
    
    i = 0
    while i < len(msg):  
        keyword = msg[i]  # 현재 문자열 시작
        j = i  # 현재 위치 저장
        
        # 🔹 사전에 존재하는 가장 긴 단어 찾기
        while j + 1 < len(msg) and keyword + msg[j + 1] in words:
            keyword += msg[j + 1]
            j += 1
        
        answer.append(words[keyword])  # 찾은 단어의 인덱스 저장

        # 🔹 새로운 단어 추가 (사전에 없으면 추가)
        if j + 1 < len(msg):  
            words[keyword + msg[j + 1]] = next_index
            next_index += 1
        
        i = j + 1  # 다음 검색 위치로 이동

    return answer
