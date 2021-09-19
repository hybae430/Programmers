# 시저 암호

def solution(s, n):
    answer = ''
    for sample in s:
        if sample == ' ':
            answer += ' '
            continue
        tmp = ord(sample) + n
        if sample.islower():
            limit = 123
        else:
            limit = 91
        answer += (chr(tmp) if tmp < limit else chr(tmp - 26))
    return answer