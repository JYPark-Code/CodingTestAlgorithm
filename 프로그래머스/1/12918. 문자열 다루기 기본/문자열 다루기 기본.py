def solution(s):
    if (s.isdigit() and len(s) == 4) or (s.isdigit() and len(s) == 6):
        return True
    else:
        return False
    