# 튜플
# 2021-10-06

def solution(s):
    answer = []
    tmp = s.lstrip('{').rstrip('}').split('},{')

    tuples = []
    for i in tmp:
        tuples.append(i.split(','))
    tuples.sort(key=len)

    for tuple in tuples:
        for i in range(len(tuple)):
            if tuple[i] not in answer:
                answer.append(tuple[i])
    return list(map(int, answer))

print(solution("{{123}}"))