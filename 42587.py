# 프린터
# 2021-09-21

def solution(priorities, location):
    wait, answer = [], []
    for idx, pr in enumerate(priorities):
        wait.append((idx, pr))

    while wait:
        idx, pr = wait.pop(0)

        if pr < max(priorities):
            priorities.append(pr)
            wait.append((idx, pr))
        else:
            answer.append(idx)
        priorities.pop(0)

    return answer.index(location) + 1

print(solution([1, 1, 9, 1, 1, 1], 0))