# 하샤드 수

def solution(x):
    tmp, answer = 0, True
    for i in str(x):
        tmp += int(i)
    if x % tmp:
        answer = False
    return answer