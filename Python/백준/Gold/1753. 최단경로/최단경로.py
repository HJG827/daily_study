import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10**9
dist = [INF] * (V + 1)
dist[K] = 0

pq = []
heapq.heappush(pq, (0, K))

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for next_node, w in graph[u]:
        nd = d + w

        if nd < dist[next_node]:
            dist[next_node] = nd
            heapq.heappush(pq, (nd, next_node))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])