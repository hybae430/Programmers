# 키패드 누르기

def solution(numbers, hand):
    answer, l, r = '', [3, 1], [3, 1]
    left, right, mid = [1, 4, 7], [3, 6, 9], [2, 5, 8, 0]
    for i in numbers:
        if i in left:
            answer += 'L'
            l = [left.index(i), 1]
        elif i in right:
            answer += 'R'
            r = [right.index(i), 1]
        else:
            m = [mid.index(i), 0]
            # com = abs(int(l[0]) - int(m[0])) + int(l[1]) - abs(int(r[0]) - int(m[0])) - int(r[1])
            com = (abs(l[0] - m[0]) + l[1]) - (abs(r[0] - m[0]) + r[1])
            print(com)
            if com > 0:
                answer += 'R'
                r = [m, 0]
            elif com < 0:
                answer += 'L'
                l = [m, 0]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = [m, 0]
                else:
                    answer += 'L'
                    l = [m, 0]
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')