# 콜라츠 추측

def solution(num):
    answer = 0
    while num != 1:
        if num % 2:
            num = num * 3 + 1
            answer += 1
        else:
            num //= 2
            answer += 1
    return answer if answer < 501 else -1