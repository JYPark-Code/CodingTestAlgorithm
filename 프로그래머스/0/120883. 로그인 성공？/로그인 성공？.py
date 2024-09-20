def solution(id_pw, db):
    # 데이터베이스에서 ID와 비밀번호 확인
    for info in db:
        if info[0] == id_pw[0]:  # ID가 일치하는지 확인
            if info[1] == id_pw[1]:  # 비밀번호도 일치하는 경우
                return "login"
            else:  # 비밀번호가 일치하지 않는 경우
                return "wrong pw"
    
    # ID가 없으면 실패
    return "fail"