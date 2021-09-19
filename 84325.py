# 직업군 추천하기
# 2021-09-13

def solution(table, languages, preference):
    highest, answer = 0, ''
    for t in table:
        tmp = 0
        spl = t.split()
        for i in range(len(languages)):
            if spl.count(languages[i]):
                tmp += preference[i] * (6 - spl.index(languages[i]))
        if tmp == highest:
            if answer > spl[0]:
                highest, answer = tmp, spl[0]
        elif tmp > highest:
            highest, answer = tmp, spl[0]
    return answer