# 문자열 압축
# 2021-09-15

def solution(s):
    shortest = 1000
    for i in range(1, len(s)//2 + 2):
        answer, idx = '', 1
        tmp = s[:i]

        for j in range(i, len(s) + i, i):
            if tmp == s[j:i+j]:
                idx += 1
            else:
                if idx == 1:
                    answer += tmp
                else:
                    answer += str(idx) + tmp
                tmp = s[j:i+j]
                idx = 1
        shortest = min(shortest, len(answer))
    return shortest

print(solution("aabbaccc"))