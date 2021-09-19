# 두 정수 사이의 합

def solution(a, b):
    if a > b:
        a, b = b, a
    return (b + a) * (b - a + 1) / 2