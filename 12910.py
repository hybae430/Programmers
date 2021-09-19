# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for i in arr:
        if not (i % divisor):
            answer.append(i)
    if not answer:
        answer.append(-1)
    else:
        answer = sorted(answer)
    return answer