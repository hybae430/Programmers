# 최댓값과 최솟값
# 2022-01-30

def solution(s):
    numbers = list(map(int, s.split()))
    return '{} {}'.format(min(numbers), max(numbers))

print(solution('-1 -2 -3 -4'))