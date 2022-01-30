# 주차 요금 계산
# 2022-01-30

from math import ceil

def solution(fees, records):
    answer = []
    rec_dict = {}
    for record in records:
        tmp = record.split()
        car_no = tmp[1]
        if car_no in rec_dict.keys():
            rec_dict[car_no].append(tmp[0])
        else:
            rec_dict[car_no] = [tmp[0]]
    rec_dict = sorted(rec_dict.items(), key=lambda x: x[0])

    for rec in rec_dict:
        tmp = 0
        if len(rec[1]) % 2:
            rec[1].append('23:59')
        while rec[1]:
            h, m = rec[1].pop(0).split(':')
            nh, nm = rec[1].pop(0).split(':')
            park_min = (int(nh) - int(h)) * 60 + (int(nm) - int(m))
            tmp += park_min
        answer.append(tmp)

    for i in range(0, len(answer)):
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            tmp = answer[i] - fees[0]
            answer[i] = fees[1] + fees[3] * ceil(tmp / fees[2])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))