# 카펫
# 2021-09-22

def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if not yellow % i:
            if brown == 2 * (i + yellow // i) + 4:
                answer = [i + 2, yellow // i + 2]
    return sorted(answer, reverse=True)

print(solution(10, 2))