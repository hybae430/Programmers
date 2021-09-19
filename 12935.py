# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) != 1:
        arr.remove(min(arr))
    else:
        arr = [-1]
    return arr