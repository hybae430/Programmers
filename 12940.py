# 최대공약수와 최소공배수

import math

def solution(n, m):
    gcd = math.gcd(n, m)
    return [gcd, (n * m) // gcd]