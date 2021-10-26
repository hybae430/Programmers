# 나머지가 1이 되는 수 찾기
# 2021-10-26

def solution(n):
    tmp = n - 1
    for i in range(2, tmp + 1):
        if not tmp % i:
            return i

print(solution(11))