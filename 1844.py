# 게임 맵 최단거리
# 2021-12-20

from collections import deque

def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    r, c = len(maps), len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]
    graph[0][0] = 1
    q = deque()
    q.append([0, 0])

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < c and 0 <= ny < r and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

    return graph[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))