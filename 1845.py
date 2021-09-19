# 폰켓몬

def solution(nums):
    kinds = set(nums)
    if len(kinds) <= (len(nums) / 2):
        answer = len(kinds)
    else:
        answer = len(nums) / 2
    return answer