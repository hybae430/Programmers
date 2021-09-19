# 오픈채팅방
# 2021-09-19

def solution(record):

    answer, arr, nname = [], [], {}
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            arr.append([tmp[1], 'E'])
            nname[tmp[1]] = tmp[2]
        elif tmp[0] == 'Leave':
            arr.append([tmp[1], 'L'])
        elif tmp[0] == 'Change':
            nname[tmp[1]] = tmp[2]

    for a in arr:
        if a[1] == 'E':
            msg = "님이 들어왔습니다."
        else:
            msg = "님이 나갔습니다."
        answer.append(nname[a[0]] + msg)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
