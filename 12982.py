# 예산

def solution(d, budget):
    answer, total = 0, 0
    d = sorted(d)
    for i in range(len(d)):
        if total + d[i] <= budget:
            total += d[i]
            answer += 1
        else:
            break
    return answer