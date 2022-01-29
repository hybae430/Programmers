# k진수에서 소수 개수 구하기
# 2022-01-2x

def isPrime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

def solution(n, k):
    nbase = ''

    if k != 10:
        while n > 0:
            n, mod = divmod(n, k)
            nbase += str(mod)
        nbase = nbase[::-1]
    else:
        nbase = str(n)

    answer = nbase.split('0')
    return sum(1 for a in answer if a != '' and isPrime(a))