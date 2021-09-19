# 이상한 문자 만들기

def solution(s):
    answer = ''
    idx = 0
    for al in s:
        if al != ' ':
            if idx % 2:
                answer += al.lower()
            else:
                answer += al.upper()
            idx += 1
        else:
            idx = 0
            answer += ' '
    return answer