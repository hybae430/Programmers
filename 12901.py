# 2016년

def solution(a, b):
    answer = ''
    cal = [(1, 'FRI')]
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    for i in range(2, 13):
        now = days.index(cal[i - 2][1])
        if cal[i - 2][0] in [1, 3, 5, 7, 8, 10, 12]:
            cal.append((i, days[now - 4]))
        elif cal[i - 2][0] in [4, 6, 9, 11]:
            cal.append((i, days[now - 5]))
        else:
            cal.append((i, days[now - 6]))

    firstday = days.index(cal[a - 1][1])
    if firstday + (b % 7 - 1) >= 0:
        answer = days[firstday + (b % 7 - 1) - 7]
    else:
        answer = days[firstday + (b % 7 - 1)]
    return answer