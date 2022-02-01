# JadenCase 문자열 만들기
# 2022-02-02

def solution(s):
    answer = ''
    is_first = True
    for sep in s:
        if is_first and sep.isalpha():
            tmp = sep.upper()
            is_first = False
        elif sep == ' ':
            is_first = True
            tmp = sep
        elif not is_first and sep.isalpha():
            tmp = sep.lower()
        else:
            is_first = False
            tmp = sep
        answer += tmp

    return answer


print(solution("3people unFollowed me"))
