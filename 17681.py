# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    tmpa, tmpb = [], []
    for i in range(n):
        tmpa.append(format(arr1[i], 'b').zfill(n))
        tmpb.append(format(arr2[i], 'b').zfill(n))
    for i in range(n):
        tmp = ''
        for j in range(n):
            if tmpa[i][j] == tmpb[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)

    return answer