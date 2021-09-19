# 복서 정렬하기
# 2021-09-13

def solution(weights, head2head):
    answer, data = [], []
    for i in range(len(weights)):
        score, fight, over = 0, 0, 0
        for j in range(len(weights)):
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    over += 1
                score += 1
                fight += 1
            elif head2head[i][j] == 'L':
                fight += 1
        if fight:
            tmp = score / fight
        else:
            tmp = 0
        data.append((tmp, over, i + 1, weights[i]))
    data = sorted(data, key = lambda x : (-x[0], -x[1], -x[3], x[2]))
    answer = [x[2] for x in data]
    return answer