# 멀쩡한 사각형
# 2021-09-23

from math import floor

def solution(w,h):
    answer = 0
    if w == 1 or h == 1:
        return answer
    elif w == h:
        return w * h - w

    for i in range(1, w):
        tmp = floor(i * h / w)
        answer += tmp

    return 2 * answer

print(solution(8, 12))