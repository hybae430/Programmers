# [1차] 다트 게임

def solution(dartResult):
    tmp, flag, res = 0, False, []
    for s in dartResult:
        if s.isdigit():
            if flag:
                tmp = int(str(tmp) + s)
            else:
                res.insert(0, tmp)
                tmp = int(s)
                flag = True
        elif s.isalpha():
            if s == 'D':
                tmp **= 2
            elif s == 'T':
                tmp **= 3
            flag = False
        elif s == '*':
            res[0] *= 2
            tmp *= 2
        elif s == '#':
            tmp *= -1

    if tmp:
        res.insert(0, tmp)

    return sum(res)