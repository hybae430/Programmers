# 신고 결과 받기
# 2022-01-2x

def solution(id_list, report, k):
    records = [[] for i in range(len(id_list))]
    answer = [0 for i in range(len(id_list))]
    for rp in report:
        fr, to = rp.split()
        i1, i2 = id_list.index(fr), id_list.index(to)
        records[i2].append(i1)

    for rc in records:
        rc = list(set(rc))
        if len(rc) >= k:
            for idx in rc:
                answer[idx] += 1

    return answer