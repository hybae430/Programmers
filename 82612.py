# 부족한 금액 계산하기

def solution(price, money, count):
    answer = price * count * (count + 1) / 2
    return answer - money if answer > money else 0