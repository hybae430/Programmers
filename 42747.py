# H-Index
# 2021-09-21

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for idx, c in enumerate(citations):
        if idx + 1 <= c:
            answer += 1
        else:
            break

    return answer

print(solution([9, 9, 9, 9, 12]))