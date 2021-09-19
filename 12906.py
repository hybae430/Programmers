# 같은 숫자는 싫어

def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)
    for i in arr:
        if tmp != i:
            answer.append(i)
            tmp = i
        else:
            pass
    return answer