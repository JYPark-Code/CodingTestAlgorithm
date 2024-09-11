def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for bb in babbling:
        valid = True
        prev_word = ""
        i = 0

        while i < len(bb):
            matched = False
            for word in words:
                # 현재 위치에서 단어가 일치하고, 이전 단어와 다른 경우
                if bb[i:i+len(word)] == word and prev_word != word:
                    matched = True
                    prev_word = word
                    i += len(word)
                    break

            if not matched:
                valid = False
                break
        
        if valid:
            answer += 1

    return answer
