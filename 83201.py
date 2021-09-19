# 상호 평가

def solution(scores):
    answer = ''
    my_scores = list(map(list, zip(*scores)))
    for i in range(len(my_scores)):
        ext = [max(my_scores[i]), min(my_scores[i])]
        for j in range(len(my_scores)):
            if (my_scores[i][i] in ext and my_scores[i].count(my_scores[i][i]) == 1):
                del my_scores[i][i]
                break
    for s in my_scores:
        avg = sum(s) / len(s)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer