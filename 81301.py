# 숫자 문자열과 영단어

def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    idx, answer = 0, ''
    while True:
        if idx > len(s) - 1:
            break
        if s[idx].isalpha():
            for i in range(3, 6):
                if s[idx:idx + i] in num.keys():
                    answer += num[s[idx:idx + i]]
                    idx += i
        else:
            answer += s[idx]
            idx += 1
    return int(answer)


print(solution("23four5six7"))
