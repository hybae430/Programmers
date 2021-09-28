# 행렬 테두리 회전하기
# 2021-09-29

def solution(rows, columns, queries):
    answer = []
    arr = [[i + j for j in range(0, columns)] for i in range(1, columns * rows + 1, columns)]

    for q in queries:
        fx, fy, lx, ly = map(int, q)
        tmp = [arr[fx - 1][fy - 1], arr[fx - 1][ly - 1], arr[lx - 1][ly - 1]]
        sm = [arr[fx - 1][fy - 1], arr[fx - 1][ly - 1], arr[lx - 1][ly - 1]]
        for i in range(fx - 1, lx):
            for j in range(fy - 1, ly):
                if j == fy - 1:
                    if i != lx - 1:
                        arr[i][j] = arr[i + 1][j]
                elif j == ly - 1:
                    if i != fx - 1:
                        arr[lx - i + fx - 1][j] = arr[lx - i + fx - 2][j]
                if i == fx - 1:
                    if j != ly - 1:
                        arr[i][ly + fy - j - 2] = arr[i][ly + fy - j - 3]
                elif i == lx - 1:
                    if j < ly - 2:
                        arr[i][j] = arr[i][j + 1]

                if i == fx - 1 or i == lx - 1 or j == fy - 1 or j == ly - 1:
                    sm.append(arr[i][j])
        arr[fx - 1][fy], arr[fx][ly - 1], arr[lx - 1][ly - 2] = tmp[0], tmp[1], tmp[2]
        answer.append(min(sm))

    return answer

print(solution(100, 97, [[1,1,100,97]]))