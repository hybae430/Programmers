# 구명보트
# 2022-05-08

def solution(people, limit):
    answer = 0
    people.sort()

    t1 = 0
    t2 = len(people) - 1
    while t1 <= t2:
        if people[t1] + people[t2] <= limit:
            t1 += 1

        t2 -= 1
        answer += 1

    return answer


print(solution([100, 500, 500, 900, 950], 1000))