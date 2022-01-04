# 후보키
# 2022-01-04

from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    evr = []
    for i in range(1, col + 1):
        evr.extend(combinations(range(col), i))

    left = []
    for e in evr:
        tmp = [tuple(item[i] for i in e) for item in relation]
        if len(set(tmp)) == row:
            left.append(e)

    answer = set(left)
    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            if len(left[i]) == len(set(left[i]) & set(left[j])):
                answer.discard(left[j])

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))