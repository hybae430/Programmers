# 괄호 변환
# 2021-09-29

def check(p):
    stack = []
    global ui
    ui = 0
    for i in range(len(p)):
        if stack:
            tmp = stack[-1]
            if tmp == '(' and p[i] == ')':
                stack.pop()
            else:
                stack.append(p[i])
        else:
            stack.append(p[i])
        if stack.count('(') == stack.count(')'):
            if not ui:
                ui = i + 1

    if stack:
        return False
    else:
        return True

def solution(p):
    global ui
    if p == '':
        return ''
    else:
        if check(p):
            return p
        else:
            u = p[:ui]
            v = p[ui:]

            if check(u):
                ans = u + solution(v)
                return ans
            else:
                tmp = u[1:-1]
                trans = tmp.maketrans('()', ')(')
                tmp = tmp.translate(trans)
                ans = '(' + solution(v) + ')' + tmp
                return ans

print(solution("()))((()"))