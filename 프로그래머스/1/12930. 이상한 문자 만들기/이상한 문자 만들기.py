def solution(s):
    answer = list()
    str_list = s.split(" ")
    # print(str_list)
    for word in str_list:
        new_word = ''
        for i in range(0, len(word)):
            if i % 2 == 0:
                up = word[i].upper()
                new_word += up
            else:
                lo = word[i].lower()
                new_word += lo
        
        answer.append(new_word)
    return " ".join(answer)