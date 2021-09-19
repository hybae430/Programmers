# 정수 내림차순으로 배치하기

def solution(n):
    tostring = list(str(n))
    return int(''.join(sorted(tostring, reverse=True)))