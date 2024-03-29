# N개의 최소공배수
# 2022-02-02

from math import gcd


def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


print(solution([2, 6, 8, 14]))