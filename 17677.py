# 뉴스 클러스터링
# 2021-09-30

from math import floor

def solution(str1, str2):
    answer = 0
    l1, l2 = [], []
    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(len(str1) - 1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            l1.append(tmp)
    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if tmp.isalpha():
            l2.append(tmp)

    if l1 == l2:
        return 65536
    else:
        tmp = list(set(l1) & set(l2))
        both = 0
        for t in tmp:
            both += min(l1.count(t), l2.count(t))
        jkd = both / (len(l1) + len(l2) - both) * 65536
        return floor(jkd)

print(solution("aa1+aa2", "AAAA12"))