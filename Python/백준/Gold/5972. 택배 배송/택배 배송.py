import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

INF = 10 ** 15

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [INF] * (N + 1)
dist[1] = 0
pq = []
heapq.heappush(pq, (1, 0))

while pq:
    node, distance = heapq.heappop(pq)

    if distance > dist[node]:
        continue
    
    for next_node, d in graph[node]:
        nd = distance + d

        if nd < dist[next_node]:
            dist[next_node] = nd
            heapq.heappush(pq, (next_node, nd))

print(dist[N])