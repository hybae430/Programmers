def solution(phone_number):
    tmp = len(phone_number) - 4
    answer = '*' * tmp + phone_number[tmp:]
    return answer


print(solution("01033334444"))