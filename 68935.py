# 3진법 뒤집기

def solution(n):
    answer = 0
    ternary = ''
    while n != 0:
        ternary += str(n % 3)
        n //= 3
    mul = len(ternary) - 1
    for i in range(len(ternary)):
        if int(ternary[i]):
            answer += int(ternary[i]) * (3 ** mul)
        mul -= 1
    return answer