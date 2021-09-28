# 타겟 넘버
# 2021-09-23

# answer = 0
#
# def DFS(idx, numbers, target, value):
#     global answer
#     n = len(numbers)
#     if idx == n and target == value:
#         answer += 1
#         return
#     elif idx == n:
#         return
#
#     DFS(idx + 1, numbers, target, value + numbers[idx])
#     DFS(idx + 1, numbers, target, value - numbers[idx])
#
# def solution(numbers, target):
#     global answer
#     DFS(0, numbers, target, 0)
#     return answer

from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution([1, 1, 1, 1, 1], 3))