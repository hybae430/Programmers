# 정수 제곱근 판별

def solution(n):
    answer = -1
    tmp = n ** (1/2)
    if int(tmp * 1000000) == int(tmp) * 1000000:
        answer = (int(tmp) + 1) ** 2
    return answer