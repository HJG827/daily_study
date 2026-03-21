import sys, heapq
input = sys.stdin.readline

INF = 10 ** 21

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

start, goal = map(int, input().split())
dist[start] = 0
q = [(0, start)]

while q:
    now_dist, node = heapq.heappop(q)

    if now_dist > dist[node]:
        continue

    for cost, next_node in graph[node]:
        next_dist = now_dist + cost

        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(q, (next_dist, next_node))

print(dist[goal])