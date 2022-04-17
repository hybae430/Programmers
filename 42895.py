# N으로 표현
# 2022-04-17

def solution(N, number):
    numbers = [0, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        tmp = {int(str(N)*i)}
        for j in range(1, i//2 + 1):
            for x in numbers[j]:
                for y in numbers[i - j]:
                    tmp.add(x + y)
                    tmp.add(x * y)
                    if x > y:
                        tmp.add(x - y)
                        tmp.add(x // y)
                    elif y > x:
                        tmp.add(y - x)
                        tmp.add(y // x)
                    else:
                        tmp.add(1)

        if number in tmp:
            return i
        elif i == 8:
            return -1
        numbers.append(tmp)

print(solution(5, 26))