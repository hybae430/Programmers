# 괄호 회전하기
# 2022-05-05

def solution(s):
    stack = []
    front = ["(", "{", "["]
    back = [")", "}", "]"]
    if len(s) % 2:  # 홀수일 경우
        return 0

    else:
        cnt = 0
        for n in range(0, len(s) - 1):
            sn, flag = 0, True
            for brk in s:
                if brk in front:
                    stack.append(brk)
                else:
                    i = back.index(brk)
                    if stack and stack[-1] == front[i]:
                        stack.pop()
                    else:
                        flag = False
                        break

                    # pop 하고 stack이 빈 경우 한세트 마감
                    if n == 0 and not stack:
                        sn += 1

            if flag:
                # 한 번에 괄호 맞을 경우
                if n == 0 and not stack:
                    return sn
                elif not stack:
                    cnt += 1

            s = (s + s[0])[1:]

    return cnt

print(solution("}}}"))