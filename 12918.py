# 문자열 다루기 기본

def solution(s):
    if (len(s) in [4, 6]) & (s.isdigit()):
        return True
    return False