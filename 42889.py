# 실패율

def solution(N, stages):
    answer, real = [], []
    total = len(stages)
    for i in range(1, N + 1):
        if total:
            p = stages.count(i)
            answer.append([i, p / total])
            total -= p
        else:
            break
    answer = sorted(answer, key = lambda item : (-item[1], item[0]))
    for a in answer:
        real.append(a[0])
    return real

print(solution(5, [2,1,2,6,2,4,3,3]))