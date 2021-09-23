# 124 나라의 숫자
# 2021-09-23

def solution(n):
    rev_base = ''
    if n <= 0:
        return '0'

    while n > 0:
        n, mod = divmod(n - 1, 3)
        if mod == 0:
            mod = 1
        elif mod == 1:
            mod = 2
        else:
            mod = 4
        rev_base += str(mod)

    rev_base = rev_base[::-1]

    return rev_base

print(solution(10))