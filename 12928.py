# 약수의 합

def solution(n):
    answer, ran = [], int(n ** (1/2)) + 1
    for i in range(1, ran):
        if not n % i:
            answer.extend([i, n // i])
    answer = list(set(answer))
    return sum(answer)