# 소수 찾기

import math
def solution(n):
    era = [False] * 2 + [True] * (n - 1)
    for i in range(2, math.ceil(math.sqrt(n))):
        if era[i]:
            for j in range(i * i, n + 1, i):
                era[j] = False
    return era.count(True)