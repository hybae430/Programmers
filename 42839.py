# 소수 찾기
# 2021-09-22

from itertools import permutations

# 여기는 에라토스테네스가 시간초과가 뜬다...;
# def era(n):
#     table = [False, False] + [True] * (n - 1)
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if table[i]:
#             for j in range(i * 2, n + 1, i):
#                 table[j] = False
#
#     return [i for i in range(2, n + 1) if table[i]]

def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        tmp = list(permutations(numbers, i))
        for j in range(len(tmp)):
            target = int(''.join(map(str, tmp[j])))
            valid = True

            if target < 2:
                continue
            else:
                for k in range(2, int(target ** 0.5) + 1):
                    if target % k == 0:
                        valid = False
                        break

            if valid:
                answer.append(target)

    return len(set(answer))

print(solution("17"))