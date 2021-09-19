# K번째수

def solution(array, commands):
    answer = []
    for l in commands:
        i, j, k = l[0], l[1], l[2]
        tmp = array[i - 1:j]
        answer.append(sorted(tmp)[k - 1])
    return answer