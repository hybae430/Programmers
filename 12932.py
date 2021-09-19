# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int, list(str(n))))
    return answer[::-1]