import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

INF = 10 ** 21
dist1 = [INF] * (N + 1)
distV1 = [INF] * (N + 1)
distV2 = [INF] * (N + 1)

v1, v2 = map(int, input().split())

pq1 = []
dist1[1] = 0
pq1.append((0, 1))
while pq1:
    dist, node = heapq.heappop(pq1)

    for d, next_node in graph[node]:
        next_dist = dist + d
        if next_dist < dist1[next_node]:
            dist1[next_node] = next_dist
            heapq.heappush(pq1, (next_dist, next_node))

pqV1 = []
distV1[v1] = 0
pqV1.append((0, v1))
while pqV1:
    dist, node = heapq.heappop(pqV1)

    for d, next_node in graph[node]:
        next_dist = dist + d
        if next_dist < distV1[next_node]:
            distV1[next_node] = next_dist
            heapq.heappush(pqV1, (next_dist, next_node))

pqV2 = []
distV2[v2] = 0
pqV2.append((0, v2))
while pqV2:
    dist, node = heapq.heappop(pqV2)

    for d, next_node in graph[node]:
        next_dist = dist + d
        if next_dist < distV2[next_node]:
            distV2[next_node] = next_dist
            heapq.heappush(pqV2, (next_dist, next_node))

pathV1 = dist1[v1] + distV1[v2] + distV2[N]
pathV2 = dist1[v2] + distV2[v1] + distV1[N]

ans = min(pathV1, pathV2)
if ans >= INF:
    print(-1)
else:
    print(ans)