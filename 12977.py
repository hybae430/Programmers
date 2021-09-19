# 소수 만들기

from itertools import combinations

# 에라토스테네스의 체
# 가장 큰 수들의 합 (범위)
n = 2997
isPrime = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):
    if isPrime[i]:
        for j in range(i * i, n + 1, i):
            if isPrime[j]:
                isPrime[j] = False
            else:
                continue


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        if isPrime[sum(i)]:
            answer += 1

    return answer