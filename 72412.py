# 순위 검색
# 2022-01-2x

from itertools import combinations
from bisect import bisect_left      # 이진탐색용 (bisect_left는 왼쪽에서의 idx 찾는 기능)

# 효율성코드 - 조건식을 전부 저장 후 점수만 이진탐색
def solution(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        info_list = info[i].split()
        ikey = info_list[:-1]
        ival = info_list[-1]

        for j in range(5):
            # 모든 경우의 수
            for c in combinations(ikey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(ival))
                else:
                    info_dict[tmp] = [int(ival)]

    for i in info_dict:
        info_dict[i].sort()

    for i in query:
        query_list = i.split()
        qkey = query_list[:-1]
        qval = query_list[-1]

        while 'and' in qkey:
            qkey.remove('and')
        while '-' in qkey:
            qkey.remove('-')
        qkey = ''.join(qkey)

        if qkey in info_dict:
            qry = info_dict[qkey]

            if qry:
                enter = bisect_left(qry, int(qval))
                answer.append(len(qry) - enter)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))