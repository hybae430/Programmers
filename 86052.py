# 빛의 경로 사이클
# 2021-10-07

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def solution(grid):
    global visited, n, m
    n = len(grid)
    m = len(grid[0])
    answer = []
    visited = [[[False] * 4 for i in range(m)] for j in range(n)]
    for x in range(n):
        for y in range(m):
            for d in range(4):
                if not visited[x][y][d]:
                    cy = simul(x, y, d, grid)
                    if cy != 0:
                        answer.append(cy)
    answer.sort()
    return answer

def simul(sx, sy, sd, grid):
    global visited
    cnt = 0
    x, y, d = sx, sy, sd
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d + 1) % 4
        elif grid[x][y] == 'L':
            d = (d - 1) % 4
        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True

print(solution(["SL", "LR"]))