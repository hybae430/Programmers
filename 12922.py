# 수박수박수박수박수박수?

def solution(n):
    if n % 2:
        return "수박" * (n // 2) + "수"
    return "수박" * (n // 2)