# 짝지어 제거하기
# 2021-09-25

def solution(s):
    stack = []
    for ch in s:
        if stack:
            tmp = stack[-1]
            if tmp == ch:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)

    if stack:
        return 0
    else:
        return 1