# 자릿수 더하기

def solution(n):
    answer = list(str(n))
    return sum(list(map(int, answer)))