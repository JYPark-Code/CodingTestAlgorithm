def solution(record):
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    users = {}
    result = []
    
    for printline in record:
        
        line = printline.split()
        
        if len(line) == 3:
            cmd, uid, username = line
            
        elif len(line) == 2:
            cmd, uid = line
        
        if cmd in ["Enter", "Change"]:
            users[uid] = username  # UID의 username을 항상 최신 값으로 갱신

        if cmd in ["Enter", "Leave"]:
            result.append((uid, message[cmd]))  # UID만 저장하고 메시지는 그대로 유지
        
    # 2. 최종적으로 users 딕셔너리의 최신 값으로 메시지 조합
    return [users[uid] + msg for uid, msg in result]