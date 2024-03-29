# 조이스틱
# 2021-10-07

def solution(name):
    name = list(name)
    answer = 0
    i = 0

    while True:
        answer += min(ord(name[i]) - 65, 91 - ord(name[i]))
        name[i] = 'A'

        if name.count('A') == len(name):
            return answer

        left, right = 1, 1
        for l in range(1, len(name)):
            if name[i - l] == 'A':
                left += 1
            else:
                break

        for r in range(1, len(name)):
            if name[i + r] == 'A':
                right += 1
            else:
                break

        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right

    return answer

print(solution("BBBAAAB"))