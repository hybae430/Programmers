# 위장
# 2021-09-20

def solution(clothes):
    cat, clist = [], []
    answer = 1
    for cloth in clothes:
        if cloth[1] in cat:
            tmp = cat.index(cloth[1])
            clist[tmp] += 1
        else:
            cat.append(cloth[1])
            clist.append(1)

    for c in clist:
        answer *= (c + 1)

    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))