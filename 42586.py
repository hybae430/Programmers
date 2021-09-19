# 기능개발

def solution(progresses, speeds):
    answer = []
    days = []
    for p in range(len(progresses)):
        if (100 - progresses[p]) % speeds[p]:
            days.append((100 - progresses[p]) // speeds[p] + 1)
        else:
            days.append((100 - progresses[p]) // speeds[p])
    cnt = 0
    tmp = days[0]
    for p in range(len(days)):
        if tmp < days[p]:
            answer.append(cnt)
            cnt = 0
            tmp = days[p]
        cnt += 1
    else:
        answer.append(cnt)

    return answer