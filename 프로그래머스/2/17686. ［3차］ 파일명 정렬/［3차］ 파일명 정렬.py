def solution(files):
    
    # (HEAD, NUMBER, 원본 파일명) 형태로 저장
    file_data = []

    for index, file in enumerate(files):
        head, number, tail = split_filename(file)
        file_data.append((head.lower(), int(number), index, file))  # HEAD는 소문자로 변환해 정렬

    # HEAD → NUMBER 기준으로 정렬
    file_data.sort(key=lambda x: (x[0], x[1], x[2]))

    # 정렬된 원본 파일명 반환
    sorted_files = [file[3] for file in file_data]

    return sorted_files


def split_filename(file):
    
    head, number, tail = "", "", ""
    num_start = False
    
    for i, char in enumerate(file):
        if char.isdigit():
            num_start = True
            if len(number) < 5:
                number += char
        elif num_start:
            tail = file[i:]
            break
        else:
            head += char
    
    return head, number, tail