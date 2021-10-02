# 거리두기 확인하기
# 2021-10-02

def solution(places):
    answer = []
    for place in places:
        cls = [['O'] * 5 for i in range(5)]
        cnt = 0
        ps = []
        for idx, arr in enumerate(place):
            for i in range(5):
                tmp = arr[i]
                if tmp == 'P':
                    cnt += 1
                    ps.append((idx, i))
                cls[idx][i] = tmp
        if not cnt:
            answer.append(1)
            continue
        else:
            res = True
            while ps and res:
                # bfs 함수 만들어서 했으면 좀 더 코드가 예뻤을텐데
                tx, ty = ps[0]
                if tx < 4 and cls[tx + 1][ty] == 'P':
                    res = False
                elif tx > 0 and cls[tx - 1][ty] == 'P':
                    res = False
                elif ty < 4 and cls[tx][ty + 1] == 'P':
                    res = False
                elif ty > 0 and cls[tx][ty - 1] == 'P':
                    res = False

                if tx < 3 and cls[tx + 2][ty] == 'P':
                    if cls[tx + 1][ty] != 'X':
                        res = False
                elif tx > 1 and cls[tx - 2][ty] == 'P':
                    if cls[tx - 1][ty] != 'X':
                        res = False
                elif ty < 3 and cls[tx][ty + 2] == 'P':
                    if cls[tx][ty + 1] != 'X':
                        res = False
                elif ty > 1 and cls[tx][ty - 2] == 'P':
                    if cls[tx][ty - 1] != 'X':
                        res = False

                if tx < 4 and ty < 4 and cls[tx + 1][ty + 1] == 'P':
                    if cls[tx + 1][ty] == cls[tx][ty + 1] == 'X':
                        res = True
                    else:
                        res = False
                if tx > 0 and ty < 4 and cls[tx - 1][ty + 1] == 'P':
                    if cls[tx - 1][ty] == cls[tx][ty + 1] == 'X':
                        res = True
                    else:
                        res = False
                if tx < 4 and ty > 0 and cls[tx + 1][ty - 1] == 'P':
                    if cls[tx + 1][ty] == cls[tx][ty - 1] == 'X':
                        res = True
                    else:
                        res = False
                if tx > 0 and ty > 0 and cls[tx - 1][ty - 1] == 'P':
                    if cls[tx - 1][ty] == cls[tx][ty - 1] == 'X':
                        res = True
                    else:
                        res = False

                if res:
                    ps.pop(0)

            if not res:
                answer.append(0)
                continue
            else:
                answer.append(1)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))