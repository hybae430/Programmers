# 체육복

def solution(n, lost, reserve):
    answer, clothes = 0, [1] * n
    # 잃어버린 사람
    for i in lost:
        clothes[i - 1] -= 1
    # 여유분 있는 사람
    for i in reserve:
        clothes[i - 1] += 1
    for i in range(n):
        # 첫번째 인덱스는 넘기기
        if not i:
            if clothes[i]:
                answer += 1
        # 여유분 있을 경우 왼쪽 확인 후 체육복 있는 사람 + 2
        elif clothes[i] == 2:
            if not clothes[i - 1]:
                clothes[i - 1], clothes[i], answer = clothes[i - 1] + 1, clothes[i] - 1, answer + 2
            else:
                answer += 1
        # 자기것만 있는 경우 체육복 있는 사람 + 1
        elif clothes[i] == 1:
            answer += 1
        # 한 개도 없을 경우 왼쪽 확인 후 체육복 있는 사람 + 2
        elif not clothes[i]:
            if clothes[i - 1] == 2:
                clothes[i - 1], clothes[i], answer = clothes[i - 1] - 1, clothes[i] + 1, answer + 1
    return answer