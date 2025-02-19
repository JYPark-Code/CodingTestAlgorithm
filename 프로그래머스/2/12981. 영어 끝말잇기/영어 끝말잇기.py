def solution(n, words):
    
    used_words = set()  # 사용된 단어 저장
    used_words.add(words[0])  # 첫 번째 단어는 자동 저장
    
    for i in range(1, len(words)):
        prev_word = words[i - 1]  # 이전 단어
        current_word = words[i]  # 현재 단어

        # (1) 끝말잇기 규칙 위반 또는 (2) 중복 단어 사용
        if current_word[0] != prev_word[-1] or current_word in used_words:
            player = (i % n) + 1  # 몇 번째 사람인지
            turn = (i // n) + 1  # 몇 번째 차례인지
            return [player, turn]  # 결과 반환
        
        used_words.add(current_word)  # 사용된 단어 기록

    return [0, 0]  # 탈락자가 없을 경우