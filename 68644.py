# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    for i in numbers:
        for j in numbers:
            answer.append(i + j)
    for i in numbers:
        answer.remove(i * 2)
    answer = list(set(answer))
    answer.sort()
    return answer