# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    count = [0] * 1025

    for i in range(1, 33):
        for j in range(1, 33):
            count[i * j] += 1

    for i in range(left, right + 1):
        if (count[i] % 2):
            answer -= i
        else:
            answer += i
        print(count[i], i, answer)

    return answer