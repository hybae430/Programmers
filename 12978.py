# 배달
# 2022-05-05

# 우선순위 큐 사용
import heapq

def dijkstra(dis, adj):
    heap = []
    # 시작 노드랑 cost 박기
    heapq.heappush(heap, [0, 1])

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost + c, n])

def solution(N, road, K):
    dis = [float('inf')] * (N + 1)
    dis[1] = 0  # 마을 1 초기화
    adj = [[] for _ in range(N + 1)]
    for r in road:
        # 양방향이기 때문에 둘다 넣어준다
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    dijkstra(dis, adj)
    return len([x for x in dis if x <= K])


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))