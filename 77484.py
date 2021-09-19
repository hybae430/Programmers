# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    down = 0
    zeros = 0
    for i in lottos:
        if i in win_nums:
            down += 1
        elif not i:
            zeros += 1
    up = down + zeros
    answer.append(rank[up])
    answer.append(rank[down])
    return answer