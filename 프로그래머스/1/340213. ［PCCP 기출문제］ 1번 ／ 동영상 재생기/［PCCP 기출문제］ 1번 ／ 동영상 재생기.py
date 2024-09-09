def solution(video_len, pos, op_start, op_end, commands):
    
    video_len = clocktoSec(video_len)
    pos = clocktoSec(pos)
    op_start = clocktoSec(op_start)
    op_end = clocktoSec(op_end)
    
    if (pos >= op_start and pos <= op_end):
            pos = op_end
            # print("첫 연산 전 입력값(op_end) : ", pos)
    
    for command in commands:

        if (command == "next"):
            pos += 10
            if pos >= video_len:
                pos = video_len
            # print("연산 후 입력값(+) : ", pos)
            
            if (pos >= op_start and pos <= op_end):
                pos = op_end
                # print("연산 후 입력값(op_end) : ", pos)
            
            continue
            
        elif (command == "prev"):
            pos -= 10
            if pos <= 0:
                pos = 0
            # print("연산 후 입력값(-) : ", pos)
            
            if (pos >= op_start and pos <= op_end):
                pos = op_end
                # print("연산 후 입력값(op_end) : ", pos)
            
            continue
        
    return sectoClock(pos)

def clocktoSec(string):
    t_min, t_sec = map(int, string.split(":"))
    return t_min * 60 + t_sec


def sectoClock(integer):
    t_min = integer // 60
    t_sec = integer % 60
    return f"{str(t_min).zfill(2)}:{str(t_sec).zfill(2)}"
    