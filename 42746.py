# 가장 큰 수
# 2021-09-21

def solution(numbers):
    numbers = list(map(str, numbers))
    tmp = sorted(numbers, key=lambda x: x*3, reverse=True)
    return str(int(''.join(tmp)))

print(solution([3, 30, 34, 5, 9]))